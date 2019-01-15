from django import forms
from lenotes.models import Group, Diary, Invitation
from markdownx.fields import MarkdownxFormField

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'name',
            'intro',
        ]
        labels = {
            'name': '群组名称',
            'intro': '群组介绍',
        }

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = [
            'content',
        ]
        labels = {
            'content' : '写下你的文章吧~',
        }
    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['content'] = MarkdownxFormField()
        self.fields['content'].label = '写下你的文章吧~'

class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['invite_id']
        labels = {'invite_id': 'Invite ID'}
    def get_id(self):
        return self.fields['invite_id'] 