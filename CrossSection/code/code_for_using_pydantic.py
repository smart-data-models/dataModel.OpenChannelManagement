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


class CrossSectionGeometry(Enum):
    Circular = 'Circular'
    Trapezoidal = 'Trapezoidal'


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


class Position(BaseModel):
    distance: Optional[float] = Field(
        None,
        description='The distance between this Entity and a reference point (e.g., the most upstream point of the system)',
    )
    refPoint: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='The reference point distance is measured from')


class Type6(Enum):
    CrossSection = 'CrossSection'


class CrossSection(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    attachedTo: Optional[
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
        description="A relationship to the ID of the channel where the cross-section 'lives in'. Reference to an entity of type Channel",
    )
    bottomSlope: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The bottom slope of the channel where the cross-section 'lives in'. All units are accepted in CEFACT code",
    )
    bottomWidth: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The bottom width of the cross-section (for 'Trapezoidal' geometry). All units are accepted in CEFACT code",
    )
    crossSectionGeometry: Optional[CrossSectionGeometry] = Field(
        None,
        description="The geometry of the cross-section. Enum:'Circular, Trapezoidal'",
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
    diameter: Optional[confloat(ge=0.0)] = Field(
        None, description='The diameter of a circular cross-section'
    )
    energyHead: Optional[float] = Field(
        None, description='The total energy head at the cross-section'
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
    inheritsFrom: Optional[
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
        description='URI of a Channel component from which the value of a property is obtained',
    )
    leftSideSlope: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The slope of the left bank of the cross-section (for 'Trapezoidal' geometry). All units are accepted in CEFACT code",
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    maxWaterDepth: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The maximum allowable water depth at the cross-section. All units are accepted in CEFACT code',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    observedBy: Optional[
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
        description='A relationship to the ID of the device that monitors raw-water properties',
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
    position: Optional[Position] = Field(
        None,
        description='Object providing information about the distance with the rest of the elements and a relationship with them',
    )
    rightSideSlope: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The slope of the right bank of the cross-section (for 'Trapezoidal' geometry). All units are accepted in CEFACT code",
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    specificConductivity: Optional[confloat(ge=0.0)] = Field(
        None, description='Water conductivity at the cross-section'
    )
    tag: Optional[str] = Field(
        None, description='An optional text string used to qualify an item'
    )
    turbidity: Optional[confloat(ge=0.0)] = Field(
        None, description='Water turbidity at the cross-section'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI-LD Entity Type. It has to be CrossSection'
    )
    waterFlow: Optional[confloat(ge=0.0)] = Field(
        None, description='Water flow at the cross-section'
    )
    waterLevel: Optional[confloat(ge=0.0)] = Field(
        None, description='Water level at the cross-section'
    )
    waterTemperature: Optional[float] = Field(
        None, description='Water temperature at the cross-section'
    )
    waterVelocity: Optional[confloat(ge=0.0)] = Field(
        None, description='Water Velocity at the cross-section'
    )
