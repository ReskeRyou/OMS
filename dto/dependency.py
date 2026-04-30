from pydantic import BaseModel, EmailStr, Field, ConfigDict

class PydanticBase(BaseModel):

    model_config = (ConfigDict(
        from_attributes=True
    ))