from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class FlowType(Enum):
    Free_Surface_flow = 'Free-Surface flow'


class GeometryType(Enum):
    Circular = 'Circular'
    Trapezoidal = 'Trapezoidal'


class Geometry(BaseModel):
    bottomSlope: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The bottom slope of the channel. All units are accepted in CEFACT code',
    )
    bottomWidth: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The bottom width of the channel (for 'Trapezoidal' geometry). All units are accepted in CEFACT code",
    )
    celerity: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Velocity of a surge propagated along the channel after the opening or close of a sluice gate',
    )
    diameter: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The diameter of a circular channel. All units are accepted in CEFACT code',
    )
    flowType: Optional[FlowType] = Field(
        None,
        description="Text defining the type of flow in the channel. Enum:'Free-Surface flow'",
    )
    geometryType: Optional[GeometryType] = Field(
        None, description="The geometry of the channel. Enum:'Trapezoidal, Circular']"
    )
    leftSideSlope: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The slope of the left bank of the channel (for 'Trapezoidal' geometry). All units are accepted in CEFACT code",
    )
    length: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The length of the channel. All units are accepted in CEFACT code',
    )
    maxWaterDepth: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The maximum allowable water depth in the channel. All units are accepted in CEFACT code',
    )
    rightSideSlope: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The slope of the right bank of the channel (for 'Trapezoidal' geometry). All units are accepted in CEFACT code",
    )
    roughnessCoefficient: Optional[confloat(ge=0.0)] = Field(
        None, description='The Manning’s roughness coefficient'
    )
    travelDuration: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The duration of the surge travelling from the downstream node (i.e., Regulation Structure) to the upstream node',
    )
    waterLoss: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Water leakages/losses from the channel - percentage of flow of the channel or a number (flow)',
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Type6(Enum):
    OpenChannel = 'OpenChannel'


class OpenChannel(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    downstreamNode: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='A relationship indicating the ID of the downstream node (e.g., Junction, Regulation Structure), where the channel ends',
    )
    geometry: Optional[Geometry] = Field(
        None, description='Description of the geometry of the channel'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tag: Optional[str] = Field(
        None, description='An optional text string used to qualify an item'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI-LD Entity Type. it has to be OpenChannel'
    )
    upstreamNode: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='A relationship indicating the ID of the upstream node (e.g., Junction, Regulation Structure), where the channel begins',
    )
