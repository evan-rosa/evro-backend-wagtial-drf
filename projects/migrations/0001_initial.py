# Generated by Django 2.2.10 on 2020-02-24 22:03

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('project_h_one', models.CharField(default='Project Name', max_length=250)),
                ('project_h_two', models.CharField(default='Project Description', max_length=250)),
                ('project_intro_p', models.TextField(blank=True)),
                ('project_p', models.CharField(default='Project Launch Date', max_length=250)),
                ('project_tech_stack_description', wagtail.core.fields.RichTextField(blank=True)),
                ('project_url', models.URLField(default='Project URL')),
                ('project_img_alt', models.CharField(default='Image Alt Text', max_length=250)),
                ('project_canonical', models.URLField(default='Canonical URL')),
                ('project_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='DsProjectsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('h_one', models.CharField(default='Project Name', max_length=250)),
                ('problem_statement', wagtail.core.fields.RichTextField(blank=True)),
                ('img_alt', models.CharField(default='Image Alt Text', max_length=250)),
                ('h_two_eda', models.CharField(default='Project Name', max_length=250)),
                ('data_summary', models.TextField(blank=True)),
                ('eda', wagtail.core.fields.RichTextField(blank=True)),
                ('model_description', wagtail.core.fields.RichTextField(blank=True)),
                ('model_result', models.TextField(blank=True)),
                ('model_conclusion', models.TextField(blank=True)),
                ('canonical', models.URLField(default='Canonical URL')),
                ('ds_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
