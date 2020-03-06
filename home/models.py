from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel, InlinePanel
from django.utils.translation import ugettext_lazy as _
from wagtail.core.blocks import BaseStreamBlock
from wagtail.core.fields import RichTextField, StreamField

from wagtail.core.models import Page, Collection, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from events.models import Event
from rooms.models import RoomPage


@register_snippet
class FooterText(models.Model):
    """
    This provides editable text for the site footer. Again it uses the decorator
    `register_snippet` to allow it to be accessible via the admin. It is made
    accessible on the template via a template tag defined in base/templatetags/
    navigation_tags.py
    """
    body = RichTextField()

    panels = [
        FieldPanel('body'),
    ]

    def __str__(self):
        return "Footer text"

    class Meta:
        verbose_name_plural = 'Footer Text'


@register_snippet
class WaterSport(models.Model):
    """"This provides editable set of water sports. This would be displayed on the home page."""
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Water Sport image'
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        help_text=_("The water sport title as you'd like it to be seen by the public")
    )
    description = RichTextField(
        null=True,
        blank=True,
        help_text=_('Write some promotional copy')
    )

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description')
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Water sports'


@register_snippet
class CafeItem(models.Model):
    """An item served in the cafe."""
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Cafe image'
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        help_text=_("The cafe item title as you'd like it to be seen by the public")
    )
    description = RichTextField(
        null=True,
        blank=True,
        help_text=_('Write some promotional copy')
    )

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description')
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'cafe items'


class HomePageSport(Orderable, models.Model):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='sport_placement')
    sport = models.ForeignKey('home.WaterSport', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Water Sport placement"
        verbose_name_plural = "Water Sport placements"

    panels = [
        SnippetChooserPanel('sport'),
    ]


class HomePageCafe(Orderable, models.Model):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='cafe_placement')
    cafe = models.ForeignKey('home.CafeItem', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Cafe placement"
        verbose_name_plural = "Cafe placements"

    panels = [
        SnippetChooserPanel('cafe'),
    ]


class HomePage(Page):
    """The Home Page, Main landing page. Is the index page of the website."""

    # Hero section of HomePage
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Homepage image')
    )
    hero_text = models.CharField(
        max_length=255,
        help_text=_('Write an introduction for the home page')
    )
    hero_cta = models.CharField(
        verbose_name='Hero CTA',
        max_length=255,
        help_text=_('Text to display on Call to Action')
    )
    hero_cta_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Hero CTA link',
        help_text=_('Choose a page to link to for the Call to Action')
    )

    about_title = models.CharField(
        verbose_name=_("About Us Section Title"),
        max_length=255,
        blank=True,
        help_text=_("Enter the title for the about us section on the home page.")
    )
    about_description = RichTextField(
        verbose_name=_("About Us Section Description"),
        blank=True,
        null=True,
        help_text=_("Enter the description for the about us section on the home page.")
    )

    sport_title = models.CharField(
        verbose_name=_("Sport Section Title"),
        max_length=255,
        blank=True,
        help_text=_("Enter the title for the water sport section on the home page.")
    )

    sport_description = RichTextField(
        verbose_name=_("Sport Section Description"),
        blank=True,
        null=True,
        help_text=_("Enter the description for the water sport section on the home page.")
    )

    cafe_title = models.CharField(
        verbose_name=_("Cafe Section Title"),
        max_length=255,
        blank=True,
        help_text=_("Enter the title for the cafe section on the home page.")
    )
    cafe_description = RichTextField(
        verbose_name=_("Cafe Section Description"),
        blank=True,
        null=True,
        help_text=_("Enter the description for the cafe section on the home page.")
    )
    contact_us_title = models.CharField(
        verbose_name=_("Contact Us Title"),
        max_length=255,
        blank=True,
        help_text=_("Enter the title of the contact us section.")
    )
    contact_us_description = RichTextField(
        verbose_name=_("Contact Us Section Description"),
        blank=True,
        null=True,
        help_text=_("Enter the description for the Contact us section on the home page.")
    )

    subpage_types = ['rooms.RoomPage', 'events.Event']

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('image'),
            FieldPanel('hero_text', classname="full"),
            MultiFieldPanel([
                FieldPanel('hero_cta'),
                PageChooserPanel('hero_cta_link'),
            ]),
        ], heading="Hero section"),
        MultiFieldPanel([
            FieldPanel('about_title'),
            FieldPanel('about_description'),
        ], heading="About us"),
        MultiFieldPanel([
            FieldPanel('sport_title'),
            FieldPanel('sport_description'),
            InlinePanel('sport_placement', label="Water Sport"),
        ], heading="Water Sports"),
        MultiFieldPanel([
            FieldPanel('cafe_title'),
            FieldPanel('cafe_description'),
            InlinePanel('cafe_placement', label="Cafe"),
        ], heading="Cafe Items"),
        MultiFieldPanel([
            FieldPanel('contact_us_title'),
            FieldPanel('contact_us_description')
        ])
    ]

    def __str__(self):
        return self.title

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request=request, *args, **kwargs)
        context['latest_event'] = Event.objects.live().latest()
        context['rooms'] = RoomPage.objects.live()
        return context
