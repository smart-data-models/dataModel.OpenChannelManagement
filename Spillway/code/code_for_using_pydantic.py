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


class SpillwayType(Enum):
    Broad_Crested = 'Broad-Crested'
    Ogee = 'Ogee'
    Sharp_Crested = 'Sharp-Crested'
    Specified_Spillway = 'Specified Spillway'


class Type6(Enum):
    Spillway = 'Spillway'


class Spillway(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    apronElevation: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The elevation at the bottom of the ogee spillway structure (P), just upstream of the spillway',
    )
    apronLength: Optional[confloat(ge=0.0)] = Field(
        None, description='The total length of the spillway bottom'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    controlCrossSection: Optional[
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
        description='A relationship indicating the ID of an entity of type Cross Section, indicating the cross section that controls the flow over the Spillway',
    )
    crestElevation: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The crest elevation of the Spillway. Required only for 'Broad-Crested', 'Ogee' and 'Sharp-Crested'",
    )
    crestLength: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The length of the Spillway equals to the total length through which water passes. Required only for 'Broad-Crested', 'Ogee' and 'Sharp-Crested'",
    )
    curveDesignDischargeCoefficient: Optional[
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
        description='The URI of an OpenChannelCurve entity that represents the design discharge coefficient (Co) as a function of apron Elevation over design upstream head (Co-P/Ho)',
    )
    curveDischargeCoefficient: Optional[
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
        description='The URI of an OpenChannelCurve entity that represents the discharge coefficient (C) as a function of upstream head (H) and spillway geometry. For instance, discharge coefficient as a function of upstream head over spillway width (C-H/L), or C/Co-H/Ho',
    )
    curveElevationDischarge: Optional[
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
        description='The URI of an OpenChannelCurve entity that represents discharge (Q) as a function of water elevation (H)',
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
    designDischarge: Optional[confloat(ge=0.0)] = Field(
        None, description='The design discharge (Qo) of the Spillway'
    )
    designDischargeCoefficient: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The discharge coefficient (Co) for energy losses for the design discharge (Ho)',
    )
    designHead: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The total upstream energy head for which the spillway is designed (Ho) for 'Ogee Spillway'",
    )
    dischargeCoefficient: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The discharge coefficient for energy losses as water enters, flows and exits the spillway',
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
    maxFloodElevation: Optional[confloat(ge=0.0)] = Field(
        None, description='The maximum elevation of water that can pass the spillway'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    numberAbutments: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The number of abutments of an ogee spillway. Only for 'Ogee' type",
    )
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
    spillwayType: Optional[SpillwayType] = Field(
        None,
        description="The type of the spillway. In the case of “Specified Spillway”, only “Elevation – discharge” curve is required. Enum:'Broad-Crested, Ogee, Sharp-Crested, Specified Spillway'",
    )
    spillwayWidth: Optional[confloat(ge=0.0)] = Field(
        None, description="The width of the spillway (m). Only for 'Broad-Crested' type"
    )
    tag: Optional[str] = Field(
        None, description='An optional text string used to qualify an item'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity Type. It has to be Spillway'
    )
    waterDischarge: Optional[confloat(ge=0.0)] = Field(
        None, description='The discharge over the spillway (Q)'
    )
