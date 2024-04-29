from django.shortcuts import render
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render,redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm, CreateRecordForm_toff,UpdateRecord_payrollForm, CreateRecordForm_schedule,UpdateRecordForm_schedule,CreateRecord_payrollForm
#from .forms import XYZ_DateInput,XYZ_DateTimeInput,XYZ_TestDataForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse,HttpRequest
import datetime

from django.db import connection
from django.db.models import F, ExpressionWrapper, FloatField
from .models import employee_record ,time_off_table, schedule_table

from django.contrib.auth.decorators import login_required

from .models import employee_record, Events,timing_table,schedule_table,time_off_table,payroll_table


def custom_query_processing(request):
    my_records = payroll_table.objects.all() 
    context = {'records': my_records}
    return render(request, 'webapp/paystub.html', context=context)

def home(request):
        return render(request, 'webapp/index.html')

def emp_payroll(request):             
       my_records = payroll_table.objects.all()  
       context = {'records': my_records}
       return render(request, 'webapp/payroll.html', context=context)        

def calc_pay(request,pk):

    data_table2 = schedule_table.objects.all()
    my_records = payroll_table.objects.get(fk_emp_id=pk)
    for entry1 in data_table2:
              if my_records.fk_emp_id == entry1.emp_id:
                result_value = entry1.total_hours * my_records.emp_payrate  
                break
    context = {'result':result_value,
               'record': my_records}
    return render(request, 'webapp/paystub1.html', context=context)
              

def my_shift(request):
       my_records = timing_table.objects.all()
       context = {'records': my_records}
       return render(request, 'webapp/workingtime.html', context=context)

def manage_schedule(request):
      my_records = schedule_table.objects.all()
      context = {'records1': my_records}
      return render(request, 'webapp/manageschedule.html', context=context)

#schedule
def schedule_shift(request):
      my_records = schedule_table.objects.all()
      context = {'records': my_records}
      return render(request, 'webapp/schedule.html', context=context)

def time_off(request):
      my_records = time_off_table.objects.all()
      context = {'records': my_records}
      return render(request, 'webapp/timeoff.html', context=context)

def timeoff_record(request, pk):
     
     all_record = time_off_table.objects.get(Timeoff_id=pk)
     context = {'records_tof': all_record}
     return render(request, 'webapp/timeoff_record.html', context=context)

def create_record_timeoff(request):
     form=CreateRecordForm_toff()

     if request.method == "POST":
          form = CreateRecordForm_toff(request.POST)
          if form.is_valid():
               form.save()
               return redirect("date-record")
          
     context = {'form': form}

     return render(request, 'webapp/create-record.html', context=context)

def singular_record_payroll(request, pk):   
     all_record = payroll_table.objects.get(fk_emp_id=pk)
     context = {'records': all_record}
     return render(request, 'webapp/view-record-payroll.html', context=context)

def update_record_payroll(request, pk):
     record = payroll_table.objects.get(fk_emp_id=pk)

     form = UpdateRecord_payrollForm(instance=record)

     if request.method == 'POST':
          form = UpdateRecord_payrollForm(request.POST, instance=record)
          if form.is_valid():
               form.save()
               return redirect("payroll")
     context = {'form':form}
     return render(request, 'webapp/update-record-payroll.html', context=context)


def create_record_payroll(request):
     form=CreateRecord_payrollForm()

     if request.method == "POST":
          form = CreateRecord_payrollForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect("payroll")
          
     context = {'form': form}

     return render(request, 'webapp/create-record-payroll.html', context=context)

def delete_record_payroll(request, pk):
    record = payroll_table.objects.get(payroll_table_id=pk)
    record.delete()
    return redirect("payroll")

def create_record_schedule(request):
     form=CreateRecordForm_schedule()

     if request.method == "POST":
          form = CreateRecordForm_schedule(request.POST)
          if form.is_valid():
               form.save()
               return redirect("date-record")
          
     context = {'form': form}

     return render(request, 'webapp/create-record.html', context=context)

def record_schedule_update(request, pk):
     record = schedule_table.objects.get(emp_id=pk)

     form = UpdateRecordForm_schedule(instance=record)

     if request.method == 'POST':
          form = UpdateRecordForm_schedule(request.POST, instance=record)
          if form.is_valid():
               form.save()
               return redirect("date-record")
     context = {'form':form}
     return render(request, 'webapp/update-record.html', context=context)

def delete_record_timeoff(request, pk):
    record = time_off_table.objects.get(Timeoff_id=pk)
    record.delete()
    return redirect("date-record")

# - Register

def register(request):
        form =  CreateUserForm()

        if request.method == "POST":
           form = CreateUserForm(request.POST)

           if form.is_valid():
               form.save()       

               return redirect("my-login")
        context = {'form': form}
        return render(request, 'webapp/register.html',context=context)

#-Login a user

def my_login(request):
      
      form = LoginForm()
      if request.method == "POST":
            form = LoginForm(request, data=request.POST)

            if form.is_valid():
                  username = request.POST.get('username')
                  password = request.POST.get('password')

                  user = authenticate(request, username=username, password=password)

                  if user is not None:
                        auth.login(request, user)

                        return redirect("dashboard")
      context = {'form': form}

      return render(request, 'webapp/my-login.html', context=context)

#- Dashboard
@login_required(login_url='my-login')
def dashboard(request):
      my_records = employee_record.objects.all()
      context = {'records': my_records}
      
      return render(request, 'webapp/dashboard.html', context=context)

# - Create a record
@login_required(login_url='my-login')
def create_record(request):
     form=CreateRecordForm()

     if request.method == "POST":
          form = CreateRecordForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect("dashboard")
          
     context = {'form': form}

     return render(request, 'webapp/create-record.html', context=context)

#- Update a record
@login_required(login_url='my-login')
def update_record(request, pk):
     record = employee_record.objects.get(emp_id=pk)

     form = UpdateRecordForm(instance=record)

     if request.method == 'POST':
          form = UpdateRecordForm(request.POST, instance=record)
          if form.is_valid():
               form.save()
               return redirect("dashboard")
     context = {'form':form}
     return render(request, 'webapp/update-record.html', context=context)

@login_required(login_url='my-login')
def singular_record(request, pk):
     
     all_record = employee_record.objects.get(emp_id=pk)
     context = {'record': all_record}
     return render(request, 'webapp/view-record.html', context=context)

# Delete a record
@login_required(login_url='my-login')
def delete_record(request, pk):
    record = employee_record.objects.get(emp_id=pk)
    record.delete()
    return redirect("dashboard")

#date selection

def create_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        start_time = timezone.now()
        end_time = timezone.now()
        Event = Events.objects.create(
            name=name,
            start_time=start_time,
            end_time=end_time
        )
        Events.save()
        return redirect('date-record')
    else:
        return render(request, 'webapp/time_date.html')

# - User Logout

def user_logout(request):
      auth.logout(request)

      return redirect("my-login")

def workingtime_new(request):
    if request.method == 'POST':
        # Capture the current date and time
        current_datetime = timezone.now()

        # Save it to your database
        record=timing_table.objects.create(punch_in=current_datetime)
        
        current_date = datetime.date.today()
        record1=timing_table.objects.create(working_day = current_date.day)
        #all_records = timing_table.objects.all()
        record2=timing_table.objects.create(punch_out=datetime.datetime.now().time())

        #record=timing_table.objects.create(punch_out=current_datetime)

        context = {'records2': record,
                   'records1': record1
                   }
        
        return render(request, 'webapp/error.html', context=context)
        
       # current_date = datetime.datetime.now()
       # timing_table.objects.create(working_day = current_date.day)
        
        # Redirect or render a response as needed
        # For instance:
        #return render(request, 'webapp/workingtime.html')

    return render(request, 'webapp/error.html', context=context)

def working_time_punchout(request):
     if request.method == 'POST':
        # Capture the current date and time
        current_datetime = timezone.now()

        # Save it to your database
        record=timing_table.objects.create(punch_out=current_datetime)
        current_date = datetime.date.today()
        record1=timing_table.objects.create(working_day = current_date.day)
        context = {'records': record,
                   'records1': record1}
        
        return render(request, 'webapp/error1.html', context=context)

     return render(request, 'webapp/error.html', context=context)

def breaktime_punchin(request):
     if request.method == 'POST':
        # Capture the current date and time
        current_datetime = timezone.now()

        # Save it to your database
        record=timing_table.objects.create(punch_in=current_datetime)
        
        current_date = datetime.date.today()
        record1=timing_table.objects.create(working_day = current_date.day)
        context = {'records2': record,
                   'records1': record1
                   }
        
        return render(request, 'webapp/error_break.html', context=context)
     return render(request, 'webapp/error.html', context=context)

def breaktime_punchout(request):
     if request.method == 'POST':
        # Capture the current date and time
        current_datetime = timezone.now()

        # Save it to your database
        record=timing_table.objects.create(punch_out=current_datetime)
        current_date = datetime.date.today()
        record1=timing_table.objects.create(working_day = current_date.day)
        context = {'records': record,
                   'records1': record1}
        
        return render(request, 'webapp/error1_break.html', context=context)

     return render(request, 'webapp/error.html', context=context)

def workingtime(request):
    #return render(request, 'webapp/workingtime.html')
    status = " "
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Punch-IN':
            request.session['punch_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status = "Punched In - Have a Great day!!"
        elif action == 'Punch-OUT':
            if 'punch_time' in request.session:
                del request.session['punch_time']
                status = "Punched Out! Good Bye"

    if 'punch_time' in request.session:
        status = "Punched In - Have a Great day!!"

    return render(request, 'webapp/Login.html', {'working_status': status})


def breaktime(request):
    status1 = " "
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Start Break':
            request.session['break_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status1 = "Battery Low - Break Started - Enjoy Your Meal!!"
        elif action == 'End Break':
            if 'break_time' in request.session:
                del request.session['break_time']
                status1 = "Battery charged - It's time to go back to work"

    if 'break_time' in request.session:
        status1 = "Battery Low - Break Started - Enjoy Your Meal!!"

    return render(request, 'webapp/break.html', {'break_status': status1})


# schedule-emp



   
