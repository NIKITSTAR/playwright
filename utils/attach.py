import allure
from allure_commons.types import AttachmentType


def add_screenshot(page):
    png = page.screenshot()
    allure.attach(body=png, name='Screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_html(page):
    html = page.content()
    allure.attach(html, name="Page HTML", attachment_type=AttachmentType.HTML)


def add_video(page):
    """После теста вызывает page.video.path(), читает .webm-файл и прикрепляет к Allure."""
    if not page.video:
        return  # Видео не включено, выходим

    video_path = page.video.path()
    with open(video_path, "rb") as f:
        video_data = f.read()

    allure.attach(
        video_data,
        name="Video",
        attachment_type=AttachmentType.WEBM,
        extension=".webm"
    )