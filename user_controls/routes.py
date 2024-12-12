from user_controls.Router import Router, DataStrategyEnum
from views.system_artifacts_page import system_artifacts_page
from views.internet_artifacts_page import internet_artifacts_page
from views.spotlight_search import spotlight_search_page
from views.user_artifacts_page import user_artifacts_page
from views.settings_page import settings_page

router = Router(DataStrategyEnum.QUERY)

router.routes = {
  "/": system_artifacts_page,
  "/internet-artifacts": internet_artifacts_page,
  "/spotlight-search": spotlight_search_page,
  "/user-artifacts": user_artifacts_page,
  "/settings": settings_page
}
