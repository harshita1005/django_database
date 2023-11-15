from django.http import JsonResponse
from django.shortcuts import render
from myapp.models import DataName
from datetime import datetime

def test_results(request):
    test_data = None  # Initialize test_data as None

    if request.method == "GET":
        search_type = request.GET.get("search_type")
        search_term = request.GET.get("search_term")
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        status = request.GET.get("status")

        if start_date:
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
            except ValueError:
                # Handle the case where the entered start_date is not a valid date
                start_date = None

        if end_date:
            try:
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
            except ValueError:
                # Handle the case where the entered end_date is not a valid date
                end_date = None

        if not start_date:
            # If start_date is not provided or not a valid date, set it to the minimum date in the database
            start_date = DataName.objects.earliest('date').date if DataName.objects.exists() else None

        if not end_date:
            # If end_date is not provided or not a valid date, set it to the maximum date in the database
            end_date = DataName.objects.latest('date').date if DataName.objects.exists() else None

        if search_term:
            if search_type == "test_name":
                test_data = DataName.objects.filter(
                    test_name__icontains=search_term,
                    test_date__range=[start_date, end_date]
                )
            elif search_type == "run_summary":
                test_data = DataName.objects.filter(
                    summary_file__icontains=search_term,
                    date__range=[start_date, end_date]
                )

        if status and test_data is not None:
            if status == "Success":
                test_data = test_data.filter(status='Succeeded Test(s)')
            elif status == "Fail":
                test_data = test_data.filter(status='Failed Test(s)')
            elif status == "Timeout":
                test_data = test_data.filter(status='Timeout Test(s)')
            elif status == "ALL":
                pass  # Do not apply status filter for "ALL" option

        if test_data is not None:
            # Explicitly order by time in ascending order
            test_data = test_data.order_by('time')
            # Reverse the order to get descending order
            test_data = list(reversed(test_data))

            # Check if no results are found
            if not test_data:
                test_data = []

    return render(request, "search_results.html", {"test_data": test_data})
