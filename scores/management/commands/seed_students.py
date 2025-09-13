import csv
from django.core.management.base import BaseCommand
from scores.models import Student
from django.db import transaction


class Command(BaseCommand):
    help = "Efficiently load student scores from a large CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to CSV file")

    def handle(self, *args, **options):
        file_path = options["csv_file"]
        batch_size = 10000   # adjust depending on your memory/DB power
        students = []

        try:
            with open(file_path, newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                count = 0

                for row in reader:
                    students.append(Student(
                        sbd=row["sbd"],
                        toan=self.parse_float(row["toan"]),
                        ngu_van=self.parse_float(row["ngu_van"]),
                        ngoai_ngu=self.parse_float(row["ngoai_ngu"]),
                        vat_li=self.parse_float(row["vat_li"]),
                        hoa_hoc=self.parse_float(row["hoa_hoc"]),
                        sinh_hoc=self.parse_float(row["sinh_hoc"]),
                        lich_su=self.parse_float(row["lich_su"]),
                        dia_li=self.parse_float(row["dia_li"]),
                        gdcd=self.parse_float(row["gdcd"]),
                        ma_ngoai_ngu=row["ma_ngoai_ngu"] or None,
                    ))

                    count += 1

                    # Insert batch when batch_size reached
                    if len(students) >= batch_size:
                        self.bulk_insert(students)
                        students.clear()
                        self.stdout.write(f"✅ Inserted {count} rows so far...")

                # Insert remaining students
                if students:
                    self.bulk_insert(students)

                self.stdout.write(self.style.SUCCESS(f"🎉 Finished importing {count} students."))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"❌ File not found: {file_path}"))

    def bulk_insert(self, students):
        # Use transaction for safety & performance
        with transaction.atomic():
            Student.objects.bulk_create(students, ignore_conflicts=True)

    def parse_float(self, value):
        try:
            return float(value) if value else None
        except ValueError:
            return None
