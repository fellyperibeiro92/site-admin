from django.db import models

class PageManager(models.Manager):
  def search(self, query):
    return self.get_queryset().filter(
      models.Q(name__icontains=query) | \
      models.Q(description__icontains=query)
    )

class Page(models.Model):

  name = models.CharField('Name', max_length=100)
  slug = models.SlugField('Slug')
  #blank=true quer dizer q o campo não é obrigatório
  description = models.TextField('Description', blank=True)
  about = models.TextField('About', blank=True)
  #null=true informa ao banco de dados q mesmo ele não sendo obrigatório, ele sempre tera um valor vazio. O banco de dados precisa dessa informação
  start_date = models.DateField('Start Date', null=True, blank=True)
  #image está ligada a MEDIA_ROOT do arquivo settings.py
  image = models.ImageField(
    upload_to='paginas/images'
    , verbose_name="Image"
    , null=True
    , blank=True
  )
  #auto_now_add vai aparecer a data somente de quando foi criada
  created_at = models.DateTimeField("Created At", auto_now_add=True)
  #auto_now_add toda vez q ela for alterada e upada, ela vai atualizar
  updated_at = models.DateTimeField("Updated At", auto_now=True)

  objects = PageManager()

  def __str__(self):
    return self.name

  @models.permalink
  def get_absolute_url(self):
    from django.core.urlresolvers import reverse
    return ('paginas:details', (), {'slug': self.slug})

  class Meta:
    verbose_name = 'Página'
    verbose_name_plural = 'Páginas'
    ordering = ['name']
    # db_table = 'users'
    # entity = models.ForeignKey(entity)
    # unique=True,
    # help_text=_(''),
    # validators=[class],
    # error_messages={
    #     'unique': _(""),
    # },
