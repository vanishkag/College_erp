from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.urls import reverse
import mysql.connector as sql
from .models import Slogin, Attendance, Achievements, Timetable, CourseAttendance, AttendanceStatus, Course,Faculty, Sis,Admins

scemail=''
spswd=''
femail=''
fpswd=''
aemail=''
apswd=''
f=0
a=0
s=0

# Create your views here.
def index(request):
    return render(request, "collegeerp/index.html")

def slogin(request):
    global scemail, spswd, s
    if request.method=='POST':
        sloginobj = sql.connect(host="localhost",user='root',passwd='123456',database='collegeerp')
        cursor=sloginobj.cursor()
        data = request.POST
        for key,value in data.items():
            if key=='scemail':
                scemail=value
            if key=='spswd':
                spswd=value
        c = "select * from slogin where scemail = '{}' and spswd = '{}'".format(scemail,spswd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request, "collegeerp/error.html") 
        else:
            c = "select regno from slogin where scemail = '{}' and spswd = '{}'".format(scemail,spswd)
            cursor.execute(c)
            r = list(cursor.fetchone())
            s = r[0]
            return stu_sis(request, s)
    return render(request, "collegeerp/slogin.html")

def fac_login(request):
    global femail, fpswd, f
    if request.method=='POST':
        floginobj = sql.connect(host="localhost",user='root',passwd='123456',database='collegeerp')
        cursor=floginobj.cursor()
        data = request.POST
        for key,value in data.items():
            if key=='femail':
                femail=value
            if key=='fpswd':
                fpswd=value
        c = "select femail, fpswd from faculty where femail = '{}' and fpswd = '{}'".format(femail,fpswd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request, "collegeerp/error.html") 
        else:
            c = "select fid from faculty where femail = '{}' and fpswd = '{}'".format(femail,fpswd)
            cursor.execute(c)
            r = list(cursor.fetchone())
            f = r[0]
            return fac_sis(request,f)
    return render(request, "collegeerp/fac_login.html")

def admin_login(request):
    global aemail, apswd, a
    if request.method=='POST':
        floginobj = sql.connect(host="localhost",user='root',passwd='123456',database='collegeerp')
        cursor=floginobj.cursor()
        data = request.POST
        for key,value in data.items():
            if key=='aemail':
                aemail=value
            if key=='apswd':
                apswd=value
        c = "select aemail, apswd from admins where aemail = '{}' and apswd = '{}'".format(aemail,apswd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request, "collegeerp/error.html") 
        else:
            c = "select aid from admins where aemail = '{}' and apswd = '{}'".format(aemail,apswd)
            cursor.execute(c)
            t=list(cursor.fetchone())
            a = t[0]
            return admin_sis(request, a)
    return render(request, "collegeerp/admin_login.html")

def admin_forpass(request):
    if request.method == 'POST':
        aemail = request.POST['aemail']
        slo = Admins.objects.get(aemail=aemail)
        oapswd = request.POST['oapswd']
        if oapswd == slo.apswd:
            apswd = request.POST['apswd']
            apswd1 = request.POST['apswd1']
            if apswd==apswd1:
                slo.apswd = apswd
                slo.save()
                return render(request, "collegeerp/admin_login.html")
    return render(request, "collegeerp/admin_forpass.html")

def welcome(request):
    return render(request, "collegeerp/welcome.html")

def error(request):
    return render(request, "collegeerp/error.html")

def stu_sis(request,r):

    students = Slogin.objects.get(regno = r)
    achievements = Achievements.objects.filter(regno = r).values()
    attendance = Attendance.objects.filter(regno = r).values()
    timetable = Timetable.objects.all()
    context = {'students' : students, 'achievements':achievements, 'timetable':timetable, 'attendance':attendance}
    return render(request, "collegeerp/stu_sis.html", context)

def stu_forpass(request):
    if request.method == 'POST':
        scemail = request.POST['scemail']
        slo = Slogin.objects.get(scemail=scemail)
        ospswd = request.POST['ospswd']
        if ospswd == slo.spswd:
            spswd = request.POST['spswd']
            spswd1 = request.POST['spswd1']
            if spswd==spswd1:
                slo.spswd = spswd
                slo.save()
                return slogin(request)
    return render(request, "collegeerp/stu_forpass.html")

def fac_sis(request,f):
    fac = Faculty.objects.get(fid=f)
    contextf = {'fac':fac}

    return render(request, "collegeerp/fac_sis.html", contextf)

def fac_forpass(request):
    if request.method == 'POST':
        femail = request.POST['femail']
        fac = Faculty.objects.get(femail=femail)
        ofpswd = request.POST['ofpswd']
        if ofpswd == fac.fpswd:
            fpswd = request.POST['fpswd']
            fpswd1 = request.POST['fpswd1']
            if fpswd==fpswd1:
                fac.fpswd = fpswd
                fac.save()
                return render(request, "collegeerp/fac_login.html")
    return render(request, "collegeerp/fac_forpass.html")

def timetable_add(request):
    if request.method == 'POST':
        time = request.POST['time']
        monday = request.POST['monday']
        tuesday = request.POST['tuesday']
        wednesday = request.POST['wednesday']
        thursday = request.POST['thursday']
        friday = request.POST['friday']
        
        timetable = Timetable.objects.create(timing=time, monday=monday, tuesday=tuesday, wednesday=wednesday, thursday=thursday, friday=friday)
        timetable.save()
        
        return fac_sis(request,f)
    
    return fac_sis(request,f)

def timetable_update(request):
    if request.method == 'POST':
        time = request.POST.get('time')
        monday = request.POST.get('monday')
        tuesday = request.POST.get('tuesday')
        wednesday = request.POST.get('wednesday')
        thursday = request.POST.get('thursday')
        friday = request.POST.get('friday')

        timetable = Timetable.objects.get(timing=time)

        timetable.timing = time
        timetable.monday = monday
        timetable.tuesday = tuesday
        timetable.wednesday = wednesday
        timetable.thursday = thursday
        timetable.friday = friday
        timetable.save()

        return fac_sis(request,f)
    
    return fac_sis(request,f)

def timetable_search(request):
    if request.method == 'POST':
        time = request.POST.get('time')
        timetable = Timetable.objects.get(timing=time)
        fac = Faculty.objects.get(fid=f)

        context = {'timetable': timetable, 'fac':fac}
        return render(request, 'collegeerp/fac_sis.html', context)
        #return fac_sis(request,f,contextf)

    return fac_sis(request,f)


def timetable_delete(request):
    if request.method == 'POST':
        time = request.POST.get('time')
        timetable = Timetable.objects.get(timing=time)
        timetable.delete()
        
    return fac_sis(request,f)


def attendance_add(request):
    if request.method == 'POST':
        # Retrieve the form data
        id = request.POST['id']
        course_id = request.POST['course']
        faculty_id = request.POST['faculty']
        branch = request.POST['branch']
        section = request.POST['section']
        attendance_date = request.POST['attendance_date']
        regno = request.POST['regno']
        status = request.POST['status']

        course = Course.objects.get(course_id=course_id)
        faculty = Faculty.objects.get(fid=faculty_id)
        course_att = CourseAttendance.objects.create(id=id, course=course, faculty=faculty, branch=branch, section=section, attendance_date=attendance_date)

        attendance_id = course_att.id
        reg = Sis.objects.get(regno=regno)
        att_status = AttendanceStatus.objects.create(attendance_id=attendance_id, regno=reg, status=status)


        return fac_sis(request,f)
    
    return fac_sis(request,f)


def attendance_update(request):
    if request.method == 'POST':
        id = request.POST['id']
        course_id = request.POST['course']
        faculty_id = request.POST['faculty']
        branch = request.POST['branch']
        section = request.POST['section']
        attendance_date = request.POST['attendance_date']
        regno = request.POST['regno']
        status = request.POST['status']

        course = Course.objects.get(course_id=course_id)
        faculty = Faculty.objects.get(fid=faculty_id)


        course_att = CourseAttendance.objects.get(id=id, course=course)
        
        reg = Sis.objects.get(regno=regno)
        att_status = AttendanceStatus.objects.get(attendance=id, regno=reg)

        course_att.id = id
        course_att.course = course
        course_att.faculty = faculty
        course_att.branch = branch
        course_att.section = section
        course_att.attendance_date = attendance_date
        att_status.regno = reg
        att_status.status = status


        course_att.save()
        att_status.save()

        return fac_sis(request,f)
    
    return fac_sis(request,f)


def attendance_search(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        att_status = AttendanceStatus.objects.get(attendance=id)
        course_att = CourseAttendance.objects.get(id=id)
        course = str(course_att.course_id)
        co_val = course.split('(')[0].strip()
        faculty = str(course_att.faculty_id)
        fac_val = int(faculty.split('(')[0].strip())
        sis = str(att_status.regno)
        sis_val = int(sis.split('(')[1].split(')')[0].strip())
        fac = Faculty.objects.get(fid=f)

        attendance_date = course_att.attendance_date.strftime("%Y-%m-%d")

        context = {'att_status': att_status, 'course_att': course_att, 'attendance_date':attendance_date, 'fac_val':fac_val, 'co_val':co_val,'sis_val':sis_val, 'fac':fac}
        return render(request, 'collegeerp/fac_sis.html', context)

    return fac_sis(request,f)


def attendance_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        att_status = AttendanceStatus.objects.get(attendance=id)
        att_status.delete()
        course_att = CourseAttendance.objects.get(id=id)
        course_att.delete()
    
    return fac_sis(request,f)

def achievement_add(request):
    if request.method == 'POST':
        id = request.POST['id']
        regno = request.POST['regno']
        achievement = request.POST['achievement']
        category = request.POST['category']
        
        reg = Sis.objects.get(regno=regno)
        ach = Achievements.objects.create(id=id, regno=reg, achievement=achievement, category=category)
        ach.save()
        
        return fac_sis(request,f)
    
    return fac_sis(request,f)

def achievement_update(request):
    if request.method == 'POST':
        id = request.POST['id']
        regno = request.POST['regno']
        achievement = request.POST['achievement']
        category = request.POST['category']

        reg = Sis.objects.get(regno=regno)

        ach = Achievements.objects.get(id=id)

        ach.regno = reg
        ach.achievement = achievement
        ach.category = category

        ach.save()

        return fac_sis(request,f)
    
    return fac_sis(request,f)


def achievement_search(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        ach = Achievements.objects.get(id=id)
        sis = str(ach.regno)
        sis_va = int(sis.split('(')[1].split(')')[0].strip())
        fac = Faculty.objects.get(fid=f)

        context = {'ach': ach, 'sis_va':sis_va, 'fac':fac}
        return render(request, 'collegeerp/fac_sis.html', context)

    return fac_sis(request,f)


def achievement_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        ach = Achievements.objects.get(id=id)
        ach.delete()
    
    return fac_sis(request,f)


def admin_sis(request,a):
    adm = Admins.objects.get(aid=a)
    context = {'adm':adm}
    return render(request, "collegeerp/admin_sis.html",context)


def sis_add(request):
    if request.method == 'POST':
        regno = request.POST['regno']
        fname = request.POST['fname']
        lname = request.POST['lname']
        scemail = request.POST['scemail']
        branch = request.POST['branch']
        section = request.POST['section']
        year = request.POST['year']
        spswd = request.POST['spswd']
        dob = request.POST['dob']
        stu_phone = request.POST['stu_phone']
        stu_email = request.POST['stu_email']
        address = request.POST['address']
        father_name = request.POST['father_name']
        father_phone = request.POST['father_phone']
        father_email = request.POST['father_email']
        mother_name = request.POST['mother_name']
        mother_phone = request.POST['mother_phone']
        mother_email = request.POST['mother_email']
        emergency1_name = request.POST['emergency1_name']
        emergency1_phone = request.POST['emergency1_phone']
        emergency2_name = request.POST['emergency2_name']
        emergency2_phone = request.POST['emergency2_phone']

        # Create the student object
        student = Sis.objects.create(
            regno=regno,
            fname=fname,
            lname=lname,
            dob=dob,
            stu_phone=stu_phone,
            stu_email=stu_email,
            address=address,
            father_name=father_name,
            father_phone=father_phone,
            father_email=father_email,
            mother_name=mother_name,
            mother_phone=mother_phone,
            mother_email=mother_email,
            emergency1_name=emergency1_name,
            emergency1_phone=emergency1_phone,
            emergency2_name=emergency2_name,
            emergency2_phone=emergency2_phone
        )
        slo = Slogin.objects.create(
            regno=regno,
            fname=fname,
            lname=lname,
            scemail=scemail,
            branch=branch,
            section=section,
            year=year,
            spswd=spswd)

        # Save the student object
        student.save()
        slo.save()

        return admin_sis(request,a)
    
    return admin_sis(request,a)


def sis_update(request):
    if request.method == 'POST':
        regno = request.POST['regno']
        fname = request.POST['fname']
        lname = request.POST['lname']
        scemail = request.POST['scemail']
        branch = request.POST['branch']
        section = request.POST['section']
        year = request.POST['year']
        spswd = request.POST['spswd']
        dob = request.POST['dob']
        stu_phone = request.POST['stu_phone']
        stu_email = request.POST['stu_email']
        address = request.POST['address']
        father_name = request.POST['father_name']
        father_phone = request.POST['father_phone']
        father_email = request.POST['father_email']
        mother_name = request.POST['mother_name']
        mother_phone = request.POST['mother_phone']
        mother_email = request.POST['mother_email']
        emergency1_name = request.POST['emergency1_name']
        emergency1_phone = request.POST['emergency1_phone']
        emergency2_name = request.POST['emergency2_name']
        emergency2_phone = request.POST['emergency2_phone']

        student = Sis.objects.get(regno=regno)
        slo = Slogin.objects.get(regno=regno)

        student.regno = regno
        student.fname = fname
        student.lname = lname
        student.dob = dob
        student.stu_phone = stu_phone
        student.stu_email = stu_email
        student.address = address
        student.father_name = father_name
        student.father_email = father_email
        student.father_phone = father_phone
        student.mother_name = mother_name
        student.mother_email = mother_email
        student.mother_phone = mother_phone
        student.emergency1_name = emergency1_name
        student.emergency1_phone = emergency1_phone
        student.emergency2_name = emergency2_name
        student.emergency2_phone = emergency2_phone

        slo.regno = regno
        slo.fname = fname
        slo.lname = lname
        slo.scemail = scemail
        slo.branch = branch
        slo.section = section
        slo.year = year
        slo.spswd = spswd

        student.save()
        slo.save()

        return admin_sis(request,a)
    
    return admin_sis(request,a)


def sis_search(request):
    if request.method == 'POST':
        regno = request.POST.get('regno')
        student = Sis.objects.get(regno=regno)
        slo = Slogin.objects.get(regno=regno)
        adm = Admins.objects.get(aid=a)


        dob = student.dob.strftime("%Y-%m-%d")

        context = {'student': student, 'slo':slo, 'dob':dob, 'adm':adm}
        return render(request, 'collegeerp/admin_sis.html', context)

    return admin_sis(request,a)


def sis_delete(request):
    if request.method == 'POST':
        regno = request.POST.get('regno')
        student = Sis.objects.get(regno=regno)
        student.delete()
        slo = Slogin.objects.get(regno=regno)
        slo.delete()
    
    return admin_sis(request,a)

def attendance(request):
    return render(request, 'collegeerp/attendance.html')
