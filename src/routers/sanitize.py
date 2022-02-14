from typing import List, Optional, Tuple,Union
from pydantic import BaseModel
from fastapi import APIRouter,HTTPException,Request
from fastapi.responses import RedirectResponse
from ..api.errors import InvalidFormatKind
from ..api.terminals.xterm import remove_xterm_ansi,remove_xterm_csi
router = APIRouter()

class AnsiFormatter(BaseModel):
    """
    Base sanitizer settings
    """
    data:str
    replace_with:str = ''
    kind    :str = 'basic',
    escape  :Optional[str] = None #might depricate
    terminal:Optional[str] = "xterm"
    
    def format(self):
        """
        filter escape sequences with the provided settings
        """
        output = None
        if self.terminal != 'xterm':
            tag = None
            if self.kind == 'all':
                tag = 'mGKHF'
            elif self.kind == 'color':
                tag = 'm'
            elif self.kind == 'moves':
                tag = "GKHF"
            elif self.kind != 'basic':
                raise InvalidFormatKind(f"'kind' must be one either 'all','color','moves',or 'basic'")
            output = remove_xterm_csi(self.data,filter=tag)
        else:
            output = remove_xterm_ansi(self.data)
        if self.escape =='escape':
            print("joumoe")
            output = (bytes(output,'UTF-8').decode('unicode_escape'))
        elif self.escape == 'unescape':
            print("jammooo")
            output = str(output).encode('unicode_escape')
        return output


@router.post("/xterm")
async def ascii_sanitize(req:Request,ascii:AnsiFormatter):
    """
    The main endpoint to filter data with
    """
    try:
        return {"sanitized": ascii.format()}
    except InvalidFormatKind as e:
        raise HTTPException(status_code=400,detail=str(e))


