from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class AccountUserManager(BaseUserManager):
	use_in_migrations = True
	
	def _create_user(self, email, password, **kwargs):
		if not email:
			raise ValueError(_('You must provide an email address'))

		email = self.normalize_email(email)
		user = self.model(email=email, **kwargs)
		user.set_password(password)
		user.save(self._db)

		return user

	def create_superuser(self, email, password, **kwargs):
		kwargs.setdefault('is_staff', True)
		kwargs.setdefault('is_superuser', True)
		kwargs.setdefault('is_active', True)

		if kwargs.get('is_staff') is not True:
			raise ValueError('Superuser must be assigned to is_staff=True')

		if kwargs.get('is_superuser') is not True:
			raise ValueError('Superuser must be assigned to is_superuser=True')

		return self._create_user(email, password, **kwargs)



class User(AbstractUser):
	"""
	An abstract class to implementing a fully featured AbtractUser model
	with admin-compliant permissions.

	Email and password are required. Other fields are optional.
    """
	username_validator = UnicodeUsernameValidator()
    
    # nullable username
	username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        null=True,
        blank=False,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
	
	email = models.EmailField(
		_('email address'),
		unique=True,
		blank=False,
		error_messages = {
			'unique': _("A user with that email address already exists.")
		}
	)

	# replaces Username with Email as the user model identifier .
	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = []

	# override
	objects = AccountUserManager()