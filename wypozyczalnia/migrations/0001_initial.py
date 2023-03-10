# Generated by Django 4.1.5 on 2023-01-23 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.IntegerField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.author')),
            ],
            options={
                'db_table': 'Book',
            },
        ),
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('copy_id', models.IntegerField(primary_key=True, serialize=False)),
                ('copy_status', models.CharField(default='na stanie', max_length=30)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.book')),
            ],
            options={
                'db_table': 'BookCopy',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.IntegerField(primary_key=True, serialize=False)),
                ('branch_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Branch',
            },
        ),
        migrations.CreateModel(
            name='LibraryUser',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('card_number', models.IntegerField(unique=True)),
                ('login', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'LibraryUser',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'Publisher',
            },
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('librarian_id', models.IntegerField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.branch')),
            ],
            options={
                'db_table': 'Librarian',
            },
        ),
        migrations.CreateModel(
            name='BookIssue',
            fields=[
                ('book_issue_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_issue', models.DateTimeField()),
                ('date_due', models.DateTimeField()),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.branch')),
                ('card_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.libraryuser')),
                ('copy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.bookcopy')),
                ('librarian_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.librarian')),
            ],
            options={
                'db_table': 'BookIssue',
            },
        ),
        migrations.AddField(
            model_name='bookcopy',
            name='branch_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.branch'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.publisher'),
        ),
    ]
