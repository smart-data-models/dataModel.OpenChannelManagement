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


class InitialCondition(BaseModel):
    targetURI: Optional[
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
        description='A relationship indicating the network component with a simulated property value',
    )
    value: Optional[Union[str, float, bool]] = None
    waterAttribute: Optional[str] = Field(
        None,
        description='Property: An attribute issued from the data models for Open Channel Management. It follows fully this data model and it could be a property or a relationship. It contains the values for specified properties, as derive from the simulation',
    )


class InputParameter(BaseModel):
    targetURI: Optional[
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
        description='A relationship indicating the network component with a simulated property value',
    )
    value: Optional[Union[str, float, bool]] = None
    waterAttribute: Optional[str] = Field(
        None,
        description='Property: An attribute issued from the data models for Open Channel Management. It follows fully this data model and it could be a property or a relationship. It contains the values for specified properties, as derive from the simulation',
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


class WaterAttribute(Enum):
    gateOpening = 'gateOpening'
    waterDischarge = 'waterDischarge'
    headDifference = 'headDifference'
    gateDischargeCoefficient = 'gateDischargeCoefficient'
    waterFlow = 'waterFlow'
    waterVelocity = 'waterVelocity'
    celerity = 'celerity'
    travelDuration = 'travelDuration'
    waterLevel = 'waterLevel'


class SimulationOutputItem(BaseModel):
    targetURI: Optional[
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
        description='A relationship indicating the network component with a simulated property value',
    )
    value: Optional[Union[str, float, bool]] = None
    waterAttribute: Optional[WaterAttribute] = Field(
        None,
        description='Property: An attribute issued from the data models for Open Channel Management. It follows fully this data model and it could be a property or a relationship. It contains the values for specified properties, as derive from the simulation',
    )


class Type6(Enum):
    RegulationStructureSimulation = 'RegulationStructureSimulation'


class RegulationStructureSimulation(BaseModel):
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
    endSimulationTime: Optional[AwareDatetime] = Field(
        None,
        description='Time of day in ISO8601 UTC format at which the simulation ends',
    )
    equivalentSluiceOpening: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Equivalent sluice gate opening in the case of multiple sluice gates, estimated as the mean value of the different openings',
    )
    estimatedGateDischargeCoefficient: Optional[confloat(ge=0.0)] = Field(
        None, description='Calibrated discharge coefficient of the sluice gate'
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
    initialConditions: Optional[List[InitialCondition]] = Field(
        None,
        description='Description of the set of the modifications to be applied to the Regulation Structure for the simulation',
    )
    inputParameters: Optional[List[InputParameter]] = Field(
        None,
        description='Description of the set of the modifications to be applied to the Regulation Structure for the simulation',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    modelError: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Percentage error between observed and simulated discharge'
    )
    modelledDischarge: Optional[confloat(ge=0.0)] = Field(
        None, description='Discharge estimated from the simulation model'
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
    simulationOutput: Optional[List[SimulationOutputItem]] = Field(
        None,
        description='Description of the set of results of simulation of the regulation structure',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    spillwayFlow: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Ratio of the spillway discharge to the new total discharge'
    )
    startSimulationTime: Optional[AwareDatetime] = Field(
        None,
        description='Time of day in ISO8601 UTC format at which the simulation begins',
    )
    targetDischarge: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Desirable discharge to be established in the channel, defined by the utility’s operators',
    )
    type: Optional[Type6] = Field(
        None,
        description='NGSI-LD Entity Type. It has to be RegulationStructureSimulation',
    )
