from typing import List, Optional

from ninja import NinjaAPI

from .models import Author, Notice, NoticeFile
from .schema import AuthorSchema, NoticeFileSchema, NoticeSchema

api = NinjaAPI(csrf=True)

@api.get("/authors", response=List[AuthorSchema])
def authors(request, first_name: Optional[str] = None):
    if first_name:
        return Author.objects.filter(title__icontains=first_name)
    return Author.objects.all()


@api.get("/notices", response=List[NoticeSchema])
def notices(request, title: Optional[str] = None):
    if title:
        return Notice.objects.filter(title__icontains=title)
    return Notice.objects.all()


@api.get("/noticefiles", response=List[NoticeFileSchema])
def notices_files(request):
    print(NoticeFile.objects.all())
    return NoticeFile.objects.all()
