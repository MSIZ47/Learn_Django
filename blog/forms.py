from django import forms
from .models import Comments,Reply,Post


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['which_post','name','email','subject','message']



class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['which_comment','message']

class CreatPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','author','category','tag','title','content','status']

    