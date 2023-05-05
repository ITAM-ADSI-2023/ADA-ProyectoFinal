from django.db import models

# Create your models here.
class Caso(models.Model):
    idcaso = models.IntegerField(db_column='idCaso', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    multimedia = models.CharField(db_column='Multimedia', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caso'
class Task(models.Model):
    idtask = models.IntegerField(db_column='idTask', primary_key=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fecha_de_inicio = models.DateField(db_column='Fecha de inicio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    facha_de_cierre = models.DateField(db_column='Facha de cierre', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    caso_idcaso = models.ForeignKey(Caso, models.DO_NOTHING, db_column='Caso_idCaso')  # Field name made lowercase.
    usuarios_idusuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_idUsuarios')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task'
        unique_together = (('idtask', 'caso_idcaso', 'usuarios_idusuarios'),)


class Usuarios(models.Model):
    idusuarios = models.IntegerField(db_column='idUsuarios', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contra = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
class UsuariosHasCaso(models.Model):
    usuarios_idusuarios = models.OneToOneField(Usuarios, models.DO_NOTHING, db_column='Usuarios_idUsuarios', primary_key=True)  # Field name made lowercase.
    caso_idcaso = models.ForeignKey(Caso, models.DO_NOTHING, db_column='Caso_idCaso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarios_has_caso'
        unique_together = (('usuarios_idusuarios', 'caso_idcaso'),)
class Comit(models.Model):
    idcomit = models.IntegerField(db_column='idComit', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    horas = models.IntegerField(db_column='Horas', blank=True, null=True)  # Field name made lowercase.
    task_idtask = models.ForeignKey('Task', models.DO_NOTHING, db_column='Task_idTask')  # Field name made lowercase.
    task_caso_idcaso = models.ForeignKey('Caso', models.DO_NOTHING, db_column='idCaso')  # Field name made lowercase.
    usuarios_idusuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_idUsuarios')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comit'
        unique_together = (('idcomit', 'task_idtask', 'task_caso_idcaso', 'usuarios_idusuarios'),)