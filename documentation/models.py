from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


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

    def get_root_doc(self):
        if self.is_root_doc:
            return self
        return (
            DocumentationPage.objects.ancestor_of(self).filter(is_root_doc=True).first()
        )
