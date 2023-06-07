from django import forms

class FormExemplo(forms.Form):
    # email = forms.EmailField(label='Email', required=True, max_length=100, min_length=5)
    # senha = forms.CharField(label='Senha', widget=forms.PasswordInput(),
    #                         max_length=16, min_length=6, required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),
                             label='Email',
                             required=True, max_length=100, min_length=5)
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
                            label='Senha',
                            max_length=16, min_length=6, required=True)
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),
                               label='Mensagem', min_length=15, max_length=1000,
                               required=True)