from django.db import models
from django.utils.translation import ugettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    TabbedInterface,
    ObjectList,
)
from wagtail.core.blocks import ChoiceBlock
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel


class RoomPage(Page):
    """This is a page that represents a room."""

    code = models.CharField(
        verbose_name=_("Room Identifier"),
        max_length=50,
        help_text=_("An Identifier for the room."),
    )
    description = RichTextField(
        verbose_name=_("Description"),
        blank=True,
        help_text=_("A short description of the room."),
    )
    price = models.DecimalField(
        verbose_name=_("Price"),
        max_digits=10,
        decimal_places=2,
        help_text=_("The room price per night."),
    )

    subpage_types = []

    def __str__(self):
        return self.title

    content_panels = Page.content_panels + [
        FieldPanel("code"),
        FieldPanel("description"),
        FieldPanel("price"),
        InlinePanel("amenities", label="Amenities"),
        InlinePanel("room_images", label="Images"),
        InlinePanel("reservations", label="Reservations"),
    ]


class Amenity(Orderable):
    """Represents amenities provided in the room."""

    room = ParentalKey(RoomPage, on_delete=models.CASCADE, related_name="amenities")
    description = RichTextField(verbose_name=_("Description"))


class RoomPageGalleryImage(Orderable):
    room = ParentalKey(RoomPage, on_delete=models.CASCADE, related_name="room_images")
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [ImageChooserPanel("image"), FieldPanel("caption")]


class Reservations(Orderable):
    """each row represents reservation for a room."""

    NEW = "new"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"
    STATUS_CHOICES = (
        (NEW, _("New")),
        (CONFIRMED, _("Confirmed")),
        (CANCELED, _("CANCELED")),
    )

    room = ParentalKey(RoomPage, on_delete=models.CASCADE, related_name="reservations")
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=50,
        default=NEW,
        help_text=_("The status of the reservation."),
    )
    price = models.DecimalField(
        verbose_name=_("Price"),
        max_digits=10,
        decimal_places=2,
        help_text=_("The price the room rented for."),
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        help_text=_("The name of the person reserving the room."),
    )

    def __str__(self):
        return f"{self.room}: {self.start_date} - {self.end_date}"

    @property
    def total_days(self):
        return (self.end_date - self.start_date).days

    panels = [
        FieldPanel("start_date"),
        FieldPanel("end_date"),
        FieldPanel("status"),
        FieldPanel("name"),
        FieldPanel("price"),
    ]
