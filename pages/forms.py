from django import forms

# ==========================================================
# 1. A classe do formulário está definida em "pages/forms.py"
# 2. Ela estende "forms.Form"
# 3. A validação ocorre quando chamamos "form.is_valid()"
# 4. clean_mensagem é executado durante o "form.is_valid()",
#    na etapa de validação dos campos.
# ==========================================================

class ContatoForm(forms.Form):
    nome = forms.CharField(
        label='Nome',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome completo'
        })
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu email'
        })
    )

    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua mensagem'
        })
    )

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if nome and len(nome.split()) < 2:
            raise forms.ValidationError(
                'Digite seu nome completo (nome e sobrenome).'
            )

        return nome