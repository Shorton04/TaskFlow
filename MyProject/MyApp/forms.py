from django import forms
from .models import User
from .models import ProjectMember, Project
from .models import Task
from django.test import TestCase

class PermissionsTestCase(TestCase):
    def setUp(self):
        self.team_leader = User.objects.create_user(username='leader', password='password', role='project_leader')
        self.team_member = User.objects.create_user(username='member', password='password', role='project_leader')
        self.project = Project.objects.create(name="Test Project", created_by=self.team_leader)

    def test_team_leader_can_create_task(self):
        self.client.login(username='leader', password='password')
        response = self.client.post('/tasks/create/', {'name': 'New Task', 'project': self.project.id})
        self.assertEqual(response.status_code, 302)  # Redirect on success

    def test_team_member_cannot_create_task(self):
        self.client.login(username='member', password='password')
        response = self.client.get('/tasks/create/')
        self.assertEqual(response.status_code, 403)  # Forbidden

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'assigned_to', 'project', 'status', 'priority', 'due_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'assigned_to': forms.Select(attrs={'class': 'form-select'}),
            'project': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class ProjectMemberForm(forms.ModelForm):
    class Meta:
        model = ProjectMember
        fields = ['user', 'role']

class ProjectForm(forms.ModelForm):
    # Form-only field for selecting members
    invite_members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Invite Members"
    )

    class Meta:
        model = Project
        fields = ['name', 'description', 'due_date']  # Do not include 'invite_members'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class AddMemberForm(forms.ModelForm):
    class Meta:
        model = ProjectMember
        fields = ['user', 'role']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
        }

class UpdateRoleForm(forms.ModelForm):
    class Meta:
        model = ProjectMember
        fields = ['role']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'role', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
        }

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['due_date', 'status', 'priority']
        widgets = {
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
        }



class PasswordChangeForm:
    pass


class DeleteAccountForm:
    pass