from typing import Any, Dict, List, Union

TemplateType = Dict[Any, Any]
TransformerObjectType = Dict[Any, Any]
TransformerType = Union[TransformerObjectType, str]
TransformerTypes = Union[List[TransformerType], TransformerType]
