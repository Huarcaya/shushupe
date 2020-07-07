# Generated by Django 3.0.8 on 2020-07-06 23:08

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('content_html', models.TextField(editable=False)),
                ('is_public', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=9)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('allow_comments', models.BooleanField(default=False)),
                ('protected_with_password', models.BooleanField()),
                ('post_password', models.CharField(blank=True, max_length=500)),
                ('pub_type', models.CharField(choices=[('article', 'Article'), ('note', 'Note'), ('page', 'Page')], default='Article', max_length=7)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pub_date',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('media_file', models.FileField(upload_to=core.models.user_directory_path)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('content_html', models.TextField(editable=False)),
                ('is_public', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=9)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('allow_comments', models.BooleanField(default=False)),
                ('protected_with_password', models.BooleanField()),
                ('post_password', models.CharField(blank=True, max_length=500)),
                ('pub_type', models.CharField(choices=[('article', 'Article'), ('note', 'Note'), ('page', 'Page')], default='Page', max_length=7)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, limit_choices_to={'parent': None}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Page')),
            ],
            options={
                'ordering': ('-pub_date',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PageComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=60)),
                ('author_email', models.EmailField(max_length=100)),
                ('author_url', models.URLField(blank=True)),
                ('author_ip', models.GenericIPAddressField(unpack_ipv4=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField()),
                ('karma', models.IntegerField(blank=True)),
                ('approved', models.BooleanField(default=False)),
                ('banned', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.PageComment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Page')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-published',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='page',
            name='tags',
            field=models.ManyToManyField(blank=True, to='core.Tag'),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('content_html', models.TextField(editable=False)),
                ('is_public', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=9)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('allow_comments', models.BooleanField(default=False)),
                ('protected_with_password', models.BooleanField()),
                ('post_password', models.CharField(blank=True, max_length=500)),
                ('pub_type', models.CharField(choices=[('article', 'Article'), ('note', 'Note'), ('page', 'Page')], default='Note', max_length=7)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='core.Tag')),
            ],
            options={
                'ordering': ('-pub_date',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=60)),
                ('author_email', models.EmailField(max_length=100)),
                ('author_url', models.URLField(blank=True)),
                ('author_ip', models.GenericIPAddressField(unpack_ipv4=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField()),
                ('karma', models.IntegerField(blank=True)),
                ('approved', models.BooleanField(default=False)),
                ('banned', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ArticleComment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Article')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-published',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='core.Tag'),
        ),
    ]
