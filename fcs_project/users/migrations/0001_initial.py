# Generated by Django 2.2.6 on 2019-10-29 16:11

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('premium_user', models.BooleanField(default=False)),
                ('account_balance', models.FloatField(default=1000.0)),
                ('commercial_user', models.BooleanField(default=False)),
                ('bank_account', models.FloatField(default=100000.0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='friend_req',
            fields=[
                ('req_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='map_to_username',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('uname', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacy', models.BooleanField(default=False)),
                ('description', models.CharField(default='None', max_length=200)),
                ('city', models.CharField(default='None', max_length=200)),
                ('phone', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sending_from', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sending_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='premium_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_plan', models.CharField(default='Silver', max_length=30)),
                ('number_of_groups', models.IntegerField(default=2)),
                ('current_number_of_groups', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poster', to='groups.Group')),
                ('posted_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='poster', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='page', max_length=30)),
                ('content', models.CharField(default='Welcome to my page!', max_length=250)),
                ('img', models.ImageField(default='None', upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='money_requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='commercial_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_groups', models.IntegerField(default=2)),
                ('current_number_of_groups', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
