# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Achievements(models.Model):
    id = models.IntegerField(primary_key=True)
    regno = models.ForeignKey('Sis', models.DO_NOTHING, db_column='regno')
    achievement = models.CharField(max_length=250)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'achievements'


class Admins(models.Model):
    aid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    aemail = models.CharField(unique=True, max_length=50, blank=True, null=True)
    apswd = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admins'


class AttendanceStatus(models.Model):
    attendance = models.OneToOneField('CourseAttendance', models.DO_NOTHING)
    regno = models.ForeignKey('Sis', models.DO_NOTHING, db_column='regno')
    status = models.CharField(max_length=1, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'attendance_status'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CollegeerpSlogin(models.Model):
    id = models.BigAutoField(primary_key=True)
    regno = models.IntegerField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    scemail = models.CharField(max_length=50)
    branch = models.CharField(max_length=20)
    section = models.CharField(max_length=3)
    year = models.IntegerField()
    spswd = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'collegeerp_slogin'


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=10)
    course_name = models.CharField(unique=True, max_length=40)
    dept_name = models.CharField(max_length=10)
    credits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course'


class CourseAttendance(models.Model):
    id = models.IntegerField(primary_key=True)
    course = models.ForeignKey(Course, models.DO_NOTHING)
    faculty = models.ForeignKey('Faculty', models.DO_NOTHING)
    branch = models.CharField(max_length=10)
    section = models.CharField(max_length=3)
    attendance_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'course_attendance'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DoneTests(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'done_tests'


class Faculty(models.Model):
    fid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    femail = models.CharField(unique=True, max_length=50)
    fpswd = models.CharField(unique=True, max_length=50)
    dept_name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'faculty'


class Notice(models.Model):
    notice_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'notice'


class Resources(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'resources'


class Sis(models.Model):
    regno = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    dob = models.DateField()
    stu_phone = models.BigIntegerField(unique=True, blank=True, null=True)
    stu_email = models.CharField(unique=True, max_length=250)
    address = models.CharField(max_length=1000)
    father_name = models.CharField(max_length=50)
    father_phone = models.BigIntegerField(unique=True, blank=True, null=True)
    father_email = models.CharField(unique=True, max_length=250)
    mother_name = models.CharField(max_length=50)
    mother_phone = models.BigIntegerField(unique=True, blank=True, null=True)
    mother_email = models.CharField(unique=True, max_length=250)
    emergency1_name = models.CharField(max_length=50)
    emergency1_phone = models.BigIntegerField(unique=True, blank=True, null=True)
    emergency2_name = models.CharField(max_length=50)
    emergency2_phone = models.BigIntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sis'


class Slogin(models.Model):
    regno = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    scemail = models.CharField(unique=True, max_length=50)
    branch = models.CharField(max_length=20)
    section = models.CharField(max_length=3)
    year = models.IntegerField()
    spswd = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'slogin'


class Timetable(models.Model):
    timing = models.CharField(primary_key=True, max_length=20)
    monday = models.CharField(max_length=10, blank=True, null=True)
    tuesday = models.CharField(max_length=10, blank=True, null=True)
    wednesday = models.CharField(max_length=10, blank=True, null=True)
    thursday = models.CharField(max_length=10, blank=True, null=True)
    friday = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timetable'


class UpcomingTests(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'upcoming_tests'

class Attendance(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=40)
    regno = models.IntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'attendance'

class Section(models.Model):
    id = models.IntegerField(primary_key=True)
    sec_id = models.CharField(max_length=3)
    semester = models.IntegerField()
    branch = models.CharField(max_length=15)

class Teaches(models.Model):
    fid = models.ForeignKey(Faculty, models.DO_NOTHING)
    course_id = models.ForeignKey(Course, models.DO_NOTHING)
    sec_id = models.ForeignKey(Section, models.DO_NOTHING)
    
