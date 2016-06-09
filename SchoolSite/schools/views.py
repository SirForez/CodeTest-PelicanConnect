from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import School, Member, Membership
from .forms import MemberForm, SchoolForm

# This is the view for the index page of the schools application
# It displays a list of all the currently saved schools
def index(request):
	SchoolsList = School.objects.order_by('name')
	context = {'schools': SchoolsList}
	return render(request, 'schools/index.html', context)

# This is a view for the member detail page of the schools application
# It displays a members name and email address
def memberDetail(request, member_id):
	try:
		# Fetch the member object from the database by member id
		member = Member.objects.get(pk=member_id)
	except member.DoesNotExist:
		raise Http404("Member does not exist")
	# Then, if no error occured, we render the view with the html template passing to it the member object
	return render(request, 'schools/memberDetail.html', {'member': member})

# This is a view for the school detail page of the schools application
# It displays the schools name and all the current members connected to that school
def schoolDetail(request, school_id):
	try:
		# Fetch the school object from the database by school id
		school = School.objects.get(pk=school_id)
		# Fetch all the members connected to the school
		members = school.members.all()
	except school.DoesNotExist:
		raise Http404("Member does not exist")
	# Then, if no error occured, we render the view with the html template passing to it both the school and members objects
	return render(request, 'schools/schoolDetail.html', {'school': school, 'members': members})

# This is the add member view of the schools application
# For a GET request, it displays an empty MemberForm
# For a POST request, it processes all the information from the generated form, and saves the member to the database
def addMember(request):
	if request.method == 'POST':
		# Since it is a post request, we get the form from the request
		form = MemberForm(request.POST)
		# Django checks if the form has been filled out and is valid
		if form.is_valid():
			# Get all the needed information from the form
			name = form.cleaned_data['memberName']
			email = form.cleaned_data['memberEmail']
			schoolname = form.cleaned_data['memberSchool']

			# Create a member object and save it to the database
			memberToAdd = Member(name=name, email=email)
			memberToAdd.save();

			# Fetch the corresponding school object
			s = School.objects.get(name=schoolname)

			# Add a membership that indicates the member is part of the corresponding school
			membershipToAdd = Membership(school=s, member=memberToAdd)
			membershipToAdd.save();

			# Redirect to index page to avoid double submissions
			return HttpResponseRedirect('/schools/')

	else:
		# Since it is a get request, we make an empty form
		form = MemberForm()

	# Render the template of the member form, passing to it the empty member form
	return render(request, 'schools/memberForm.html', {'form': form})

# This is the add member view of the schools application
# For a GET request, it displays an empty SchoolForm
# For a POST request, it processes all the information from the generated form, and saves the school to the database
def addSchool(request):
	if request.method == 'POST':
		# Since it is a post request, we get the form from the request
		form = SchoolForm(request.POST)
		# Django checks if the form has been filled out and is valid
		if form.is_valid():
			# Fetch the needed information from the form
			name = form.cleaned_data['schoolName']

			# Create a school object and save it to the database
			schoolToAdd = School(name=name)
			schoolToAdd.save();

			# Redirect to index page to avoid double submissions
			return HttpResponseRedirect('/schools/')

	else:
		# Since it is a get request, we make an empty form
		form = SchoolForm()

	# Render the template of the school form, passing to it the empty school form
	return render(request, 'schools/schoolForm.html', {'form': form})