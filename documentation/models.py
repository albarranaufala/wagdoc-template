from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import (
    BaseSiteSetting,
    register_setting,
)
from wagtail.images import get_image_model


class DocumentationPage(Page):
    body = RichTextField(
        null=True,
        blank=True,
        features=[
            "h2",
            "bold",
            "italic",
            "link",
            "document-link",
            "ol",
            "ul",
            "hr",
            "image",
            "code",
            "blockquote",
        ],
    )
    is_root_doc = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("is_root_doc"),
    ]

    subpage_types = ["documentation.DocumentationPage"]

    def get_root_doc(self):
        if self.is_root_doc:
            return self
        return (
            DocumentationPage.objects.ancestor_of(self).filter(is_root_doc=True).first()
        )

    def get_next_doc(self):
        first_child = self.get_children().live().in_menu().first()
        if first_child:
            return first_child
        next_sibling = self.get_next_siblings().live().in_menu().first()
        if next_sibling:
            return next_sibling
        return None

    def get_prev_doc(self):
        if self.is_root_doc:
            return None
        prev_sibling = self.get_prev_siblings().live().in_menu().first()
        if prev_sibling:
            return prev_sibling
        parent = self.get_parent()
        if not getattr(parent, "is_root_doc", False):
            return parent
        return None


@register_setting
class AppSettings(BaseSiteSetting):
    app_logo = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("app_logo"),
    ]
