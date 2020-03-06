from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel


class Event(Page):
    """This is a page that represents an event."""

    promo_line = RichTextField(
        verbose_name=_("Promo Line"),
        blank=True,
        help_text=_("A short promo line of the event."),
    )
    description = RichTextField(
        verbose_name=_("Description"),
        blank=True,
        help_text=_("A short description of the event."),
    )
    start_date = models.DateField(verbose_name=_("Start Date"), null=True, blank=True)
    end_date = models.DateField(verbose_name=_("End Date"), null=True, blank=True)
    promo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Event promo image')
    )

    subpage_types = []

    def __str__(self):
        return self.title

    content_panels = Page.content_panels + [
        FieldPanel('promo_line'),
        FieldPanel('description'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        ImageChooserPanel('promo_image'),
        InlinePanel("event_images", label="Images"),
    ]

    class Meta:
        get_latest_by = ['-start_date']


class RoomPageGalleryImage(Orderable):
    page = ParentalKey(Event, on_delete=models.CASCADE, related_name="event_images")
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [ImageChooserPanel("image"), FieldPanel("caption")]

