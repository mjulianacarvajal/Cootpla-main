
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm

from django.contrib.auth.models import User

from .models import Encomienda, Sede, Vehiculo, Programacion, Conductor, Venta
from datetime import datetime

class RegistrarUsuario(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text="El sistema requiere un correo electrónico para asignar un nuevo usuario.")
    first_name = forms.CharField(max_length=250, help_text="El sistema requiere un nombre para completar los datos.")
    last_name = forms.CharField(max_length=250, help_text="El sistema requiere un apellido para completar los datos.")

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"{user.email} es un correo ya existente en el sistema")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"{user.username} es un usuario ya existente en el sistema")




class ActualizarContrasena(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm rounded-0'}),
        label="Contraseña Anterior")
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm rounded-0'}),
        label="Nueva Constraseña")
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm rounded-0'}),
        label="Confirmar Nueva Contraseña")

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class ActualizarPerfil(UserChangeForm):
    username = forms.CharField(max_length=250, help_text="Asignar un usuario es requerido.")
    email = forms.EmailField(max_length=250, help_text="Asignar un correo electronico es requerido.")
    first_name = forms.CharField(max_length=250, help_text="Asignar un nombre para este usuario es requerido.")
    last_name = forms.CharField(max_length=250, help_text="Asignar  un apellido para este usuario es requerido.")
    current_password = forms.CharField(max_length=250)


    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

    def clean_current_password(self):
        if not self.instance.check_password(self.cleaned_data['current_password']):
            raise forms.ValidationError(f"Contraseña Incorrecta")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"{user.email} es un correo ya existente en el sistema")

    def clean_username(self):

        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"{user.username} es un nick ya existente en el sistema")


#sedes

class GuardarSede(forms.ModelForm):
    sede = forms.CharField(max_length="25")
    tipo = forms.ChoiceField(choices=[('1', 'Terminal'), ('2', 'Oficina'), ('3', 'Paradero')])

    class Meta:
        model = Sede
        fields = ('sede', 'tipo',)

    def clean_sede(self):
        id = self.instance.id if self.instance.id else 0
        sede = self.cleaned_data['sede']

        try:
            if int(id) > 0:
                loc = Sede.objects.exclude(id=id).get(sede=sede)
            else:
                loc = Sede.objects.get(sede=sede)
        except:
            return sede

        raise forms.ValidationError(f"{sede} Sede ya existente en el sistema.")


class GuardarVehiculo(forms.ModelForm):
    placa_veh = forms.CharField(max_length=6)
    class Meta:
        model = Vehiculo
        fields = ('propietario', 'numero_veh', 'placa_veh', 'asientos', 'estado')


    def clean_numero_veh(self):
        id = self.instance.id if self.instance.id else 0
        numero_veh = self.cleaned_data['numero_veh']
        # print(int(id) > 0)
        try:
            if int(id) > 0:
                vehiculo = Vehiculo.objects.exclude(id=id).get(numero_veh=numero_veh)
            else:
                vehiculo = Vehiculo.objects.get(numero_veh=numero_veh)
        except:
            return numero_veh

        raise forms.ValidationError(f"{numero_veh}: Este vehiculo ya existe en sistema")

    def clean_placa_vehiculo(self):
        id = self.instance.id if self.instance.id else 0
        placa_veh = self.cleaned_data['placa_veh']
        # print(int(id) > 0)
        try:
            if int(id) > 0:
               placa_ = Vehiculo.objects.exclude(id=id).get(placa_veh=placa_veh)
            else:
               placa_ = Vehiculo.objects.get(placa_veh=placa_veh)
        except:
            return placa_veh
            #  placa_veh.upper()   #si me arroja mayus no me valida la placa
        raise forms.ValidationError(f"{placa_veh}: Esta placa ya existe en sistema")

    def clean_placa_mayusc(self):
        placa_veh = self.cleaned_data['placa_veh']
        return placa_veh.upper()


class GuardarProgramacion(forms.ModelForm):
    codigo = forms.CharField(max_length="250")
    programacion = forms.CharField()
    conductor = forms.ModelChoiceField(queryset=Conductor.objects.all(), required=True)
    estado =forms.ChoiceField(choices=[('0','Cancelado'),('1', 'Programado'),('2', 'Despachado')])

    class Meta:
        model = Programacion
        fields = ('codigo', 'vehiculo', 'origen', 'destino', 'precio', 'programacion', 'estado', 'conductor')


    def clean_codigo(self):
        id = self.instance.id if self.instance.id else 0
        if id > 0:
            try:
                programacion = Programacion.objects.get(id=id)
                return programacion.codigo
            except:
                
                codigo = ''
        else:
            codigo = ''
        pref = datetime.today().strftime('%Y%m%d')
        codigo = str(1).zfill(4)
        while True:
            prog = Programacion.objects.filter(codigo=str(pref + codigo)).count()
            if prog > 0:
                codigo = str(int(codigo) + 1).zfill(4)
            else:
                codigo = str(pref + codigo)
                break
        return codigo



## venta
class GuardarVenta(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ('codigo_compra', 'comprador', 'documento', 'programacion_venta', 'asientos_compra', 'estado',)


    def clean_codigo_compra(self):
        id = self.instance.id if self.instance.id else 0
        if id > 0:
            try:
                venta = Venta.objects.get(id=id)
                return venta.codigo_compra
            except:
                codigo_compra = ''
        else:
            codigo_compra = ''
        pref = datetime.today().strftime('%Y%m%d')
        codigo = str(1).zfill(4)
        while True:
            prog = Venta.objects.filter(codigo_compra=str(pref + codigo_compra)).count()
            if prog > 0:
                codigo_compra = str(int(codigo_compra) + 1).zfill(4)
            else:
                codigo_compra = str(pref + codigo_compra)
                break
        return codigo_compra


class CancelarVenta(forms.ModelForm):
   
    class Meta:
        model = Venta
        fields = ('estado',)


class GuardarEncomienda(forms.ModelForm):

    class Meta:
        model = Encomienda
        fields = (
            'programacion', 'nombre_envio', 'cedula_envio',
            'telefono_envio', 'nombre_recibido','cedula_recibido',
            'telefono_recibido','costo_envio','estado',
        )
