from django.shortcuts import render
from django.db.models import Count, Q, F, Sum, FloatField
from .models import Student
from .subjects import Subject
from .forms import CheckScoreForm
# Create your views here.

# home view
def home(request):
    return render(request, "scores/home.html")

# check score view
def check_score(request):
    form = CheckScoreForm(request.GET or None)   # ?sbd=...
    student = None
    error = None

    if request.GET and form.is_valid():  # only run if form submitted
        sbd = form.cleaned_data['sbd']
        try:
            student = Student.objects.get(sbd=sbd)
        except Student.DoesNotExist:
            error = f"No student found with registration number: {sbd}"

    return render(request, "scores/check_score.html", {
        "form": form,
        "student": student,
        "error": error,
    })

# report view
import logging
from django.shortcuts import render
from django.db.models import Count, Q
from django.http import HttpResponseServerError

logger = logging.getLogger(__name__)

def report(request):
    subjects = [
        Subject("toan", "Toán"),
        Subject("ngu_van", "Ngữ Văn"),
        Subject("ngoai_ngu", "Ngoại Ngữ"),
        Subject("vat_li", "Vật Lý"),
        Subject("hoa_hoc", "Hóa Học"),
        Subject("sinh_hoc", "Sinh Học"),
        Subject("lich_su", "Lịch Sử"),
        Subject("dia_li", "Địa Lý"),
        Subject("gdcd", "GDCD"),
    ]

    labels = []
    data_8 = []
    data_6_8 = []
    data_4_6 = []
    data_lt4 = []

    try:
        for subject in subjects:
            try:
                result = Student.objects.aggregate(
                    gte8=Count(
                        subject.field_name,
                        filter=Q(**{f"{subject.field_name}__gte": 8}),
                    ),
                    gte6lt8=Count(
                        subject.field_name,
                        filter=Q(
                            **{
                                f"{subject.field_name}__gte": 6,
                                f"{subject.field_name}__lt": 8,
                            }
                        ),
                    ),
                    gte4lt6=Count(
                        subject.field_name,
                        filter=Q(
                            **{
                                f"{subject.field_name}__gte": 4,
                                f"{subject.field_name}__lt": 6,
                            }
                        ),
                    ),
                    lt4=Count(
                        subject.field_name,
                        filter=Q(**{f"{subject.field_name}__lt": 4}),
                    ),
                )

                labels.append(subject.display_name)
                data_8.append(result.get("gte8", 0))
                data_6_8.append(result.get("gte6lt8", 0))
                data_4_6.append(result.get("gte4lt6", 0))
                data_lt4.append(result.get("lt4", 0))

            except Exception as e:
                # Handle per-subject failure without breaking the whole loop
                logger.error(f"Error processing subject {subject.field_name}: {e}")
                labels.append(subject.display_name)
                data_8.append(0)
                data_6_8.append(0)
                data_4_6.append(0)
                data_lt4.append(0)

        context = {
            "labels": labels,
            "data_8": data_8,
            "data_6_8": data_6_8,
            "data_4_6": data_4_6,
            "data_lt4": data_lt4,
        }
        return render(request, "scores/report.html", context)

    except Exception as e:
        # Handle total failure gracefully
        logger.critical(f"Report generation failed: {e}", exc_info=True)
        return HttpResponseServerError("An error occurred while generating the report.")


# top 10 students view
def top_group_a(request):
    try:
        students = (
            Student.objects
            .filter(toan__isnull=False, vat_li__isnull=False, hoa_hoc__isnull=False)  # only full scores
            .annotate(
                total_group_a=F("toan") + F("vat_li") + F("hoa_hoc")
            )
            .order_by("-total_group_a")[:10]
        )
    except Exception as e:
        students = []
        print("Error fetching top Group A students:", e)


    return render(request, "scores/top_group_a.html", {"students": students})
