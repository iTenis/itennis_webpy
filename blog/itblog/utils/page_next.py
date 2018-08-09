from .preset import preset_str
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_pages(totalpage=1, current_page=1):
    """
    example: get_pages(10,1) result=[1,2,3,4,5]
    example: get_pages(10,9) result=[6,7,8,9,10]
    页码个数由WEB_DISPLAY_PAGE设定
    """
    WEB_DISPLAY_PAGE = 5
    front_offset = int(WEB_DISPLAY_PAGE / 2)
    if WEB_DISPLAY_PAGE % 2 == 1:
        behind_offset = front_offset
    else:
        behind_offset = front_offset - 1

    if totalpage < WEB_DISPLAY_PAGE:
        return list(range(1, totalpage + 1))
    elif current_page <= front_offset:
        return list(range(1, WEB_DISPLAY_PAGE + 1))
    elif current_page >= totalpage - behind_offset:
        start_page = totalpage - WEB_DISPLAY_PAGE + 1
        return list(range(start_page, totalpage + 1))
    else:
        start_page = current_page - front_offset
        end_page = current_page + behind_offset
        return list(range(start_page, end_page + 1))


def page_obj(objs, currentnum, perpagenum):
    paginator_obj = Paginator(objs, perpagenum)
    page_obj = paginator_obj.page(currentnum)
    total_page_number = paginator_obj.num_pages
    page_list = get_pages(int(total_page_number), int(currentnum))
    context = preset_str(page_obj=page_obj, page_list=page_list)
    return context
