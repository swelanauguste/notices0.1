from ninja import ModelSchema, Schema
from ninja.orm import create_schema

from .models import Author, Notice, NoticeFile


class NotFoundSchema(Schema):
    message: str


NoticeSchema = create_schema(Notice)
NoticeFileSchema = create_schema(NoticeFile)
AuthorSchema = create_schema(Author, exclude=["tel"])

# class NoticeSchema(ModelSchema):
#     class Config:
#         model = Notice
#         model_fields = [
#             "created_at",
#             "updated_at",
#             "id",
#             "status",
#             "category",
#             "title",
#             "slug",
#             "content",
#             "author",
#         ]
