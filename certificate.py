from io import BytesIO
from typing import Optional
from PIL import Image, ImageDraw, ImageFont,UnidentifiedImageError
from base64 import b64encode, b64decode


#certificate template
async def generate_certificate(index: str, org: str, logo: str, name: str):
    div={
        "1":{
            "nameColor":"black",
            "namePos":(1000,707),
            "orgColor":"black",
            "oPos":(540,1145),
        },
        "2":{
            "nameColor":"black",
            "namePos":(1000,706),
            "orgColor":"black",
            "oPos":(540,1145),
        },
        "3":{
            "nameColor":"black",
            "namePos":(1000,760),
            "orgColor":"black",
            "oPos":(540,1145),

        },
        "4":{
            "nameColor":"black",
            "namePos":(1000,760),
            "orgColor":"black",
            "oPos":(540,1145),

        },
        "5":{
            "nameColor":"black",
            "namePos":(1000,760),
            "orgColor":"black",
            "oPos":(540,1145),

        }
    }


    font1=ImageFont.truetype("Cardo-Bold.ttf",size=100)
    font2=ImageFont.truetype("Lato-Black.ttf",size=65)
    img=Image.open(img)
    draw=ImageDraw.Draw(img)
    draw.text(div[index]["namePos"],name,fill=div[index]["nameColor"],font=font1,anchor="ms")
    draw.text(div[index]["oPos"],org,fill=div[index]["orgColor"],font=font2,anchor="ms")
    

    try:
        logo=b64decode(logo)
        logoimg=Image.open(BytesIO(logo))
        img.paste(logoimg,(1700,140),logoimg)
    except UnidentifiedImageError:
        pass

    buffered=BytesIO()
    img.save(buffered,format="png")
    certificate=b64encode(buffered.getvalue()).decode("utf-8")
    return {
        "file":certificate,
        "filename":f"{name}",
        "filetype":"images/png"
    }