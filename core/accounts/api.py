from ninja import Router

router = Router()

@router.get("/none")
def home(request):
    return "a boy is crying" 