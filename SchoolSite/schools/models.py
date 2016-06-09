from django.db import models

# Member model class, includes name and email
class Member(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    def __str__(self):
    	return self.name + ", email:"+ self.email

# School model class, includes name and a many to many field of members, i.e. a list of members
class School(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Member,
        through='Membership',
        through_fields=('school', 'member'),
    )
    def __str__(self):
    	return self.name

# Membership model class, this is used to connect Member and School in a many to many relationship
class Membership(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)