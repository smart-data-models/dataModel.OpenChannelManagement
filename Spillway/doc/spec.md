<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: Spillway  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/Spillway/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **This entity contains a harmonised description for a generic Spillway made for Raw-Water (Open Channels) System Management domain. Spillway represents a junction-type object, controlling the release of water from a dam or regulation structure downstream.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: An alternative name for this item  - `apronElevation[number]`: The elevation at the bottom of the ogee spillway structure (P), just upstream of the spillway.  - `apronLength[number]`: The total length of the spillway bottom  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `controlCrossSection[*]`: A relationship indicating the ID of an entity of type Cross Section, indicating the cross section that controls the flow over the Spillway.  - `crestElevation[number]`: The crest elevation of the Spillway. Required only for 'Broad-Crested', 'Ogee' and 'Sharp-Crested'  - `crestLength[number]`: The length of the Spillway equals to the total length through which water passes. Required only for 'Broad-Crested', 'Ogee' and 'Sharp-Crested'  - `curveDesignDischargeCoefficient[*]`: The URI of an OpenChannelCurve entity that represents the design discharge coefficient (Co) as a function of apron Elevation over design upstream head (Co-P/Ho).  - `curveDischargeCoefficient[*]`: The URI of an OpenChannelCurve entity that represents the discharge coefficient (C) as a function of upstream head (H) and spillway geometry. For instance, discharge coefficient as a function of upstream head over spillway width (C-H/L), or C/Co-H/Ho.  - `curveElevationDischarge[*]`: The URI of an OpenChannelCurve entity that represents discharge (Q) as a function of water elevation (H).  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description[string]`: A description of this item  - `designDischarge[number]`: The design discharge (Qo) of the Spillway  - `designDischargeCoefficient[number]`: The discharge coefficient (Co) for energy losses for the design discharge (Ho).  - `designHead[number]`: The total upstream energy head for which the spillway is designed (Ho) for 'Ogee Spillway'  - `dischargeCoefficient[number]`: The discharge coefficient for energy losses as water enters, flows and exits the spillway  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `maxFloodElevation[number]`: The maximum elevation of water that can pass the spillway.  - `name[string]`: The name of this item.  - `numberAbutments[number]`: The number of abutments of an ogee spillway. Only for 'Ogee' type.  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `spillwayType[string]`: The type of the spillway. In the case of “Specified Spillway”, only “Elevation – discharge” curve is required. Enum:'Broad-Crested, Ogee, Sharp-Crested, Specified Spillway'.  - `spillwayWidth[number]`: The width of the spillway (m). Only for 'Broad-Crested' type  - `tag[string]`: An optional text string used to qualify an item  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI Entity Type. It has to be Spillway.  - `waterDischarge[number]`: The discharge over the spillway (Q)  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `location`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Spillway:    
  description: 'This entity contains a harmonised description for a generic Spillway made for Raw-Water (Open Channels) System Management domain. Spillway represents a junction-type object, controlling the release of water from a dam or regulation structure downstream.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    apronElevation:    
      description: 'The elevation at the bottom of the ogee spillway structure (P), just upstream of the spillway.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    apronLength:    
      description: 'The total length of the spillway bottom'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    controlCrossSection:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of an entity of type Cross Section, indicating the cross section that controls the flow over the Spillway.'    
      x-ngsi:    
        type: Relationship    
    crestElevation:    
      description: 'The crest elevation of the Spillway. Required only for ''Broad-Crested'', ''Ogee'' and ''Sharp-Crested'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    crestLength:    
      description: 'The length of the Spillway equals to the total length through which water passes. Required only for ''Broad-Crested'', ''Ogee'' and ''Sharp-Crested'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    curveDesignDischargeCoefficient:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The URI of an OpenChannelCurve entity that represents the design discharge coefficient (Co) as a function of apron Elevation over design upstream head (Co-P/Ho).'    
      x-ngsi:    
        type: Relationship    
    curveDischargeCoefficient:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The URI of an OpenChannelCurve entity that represents the discharge coefficient (C) as a function of upstream head (H) and spillway geometry. For instance, discharge coefficient as a function of upstream head over spillway width (C-H/L), or C/Co-H/Ho.'    
      x-ngsi:    
        type: Relationship    
    curveElevationDischarge:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The URI of an OpenChannelCurve entity that represents discharge (Q) as a function of water elevation (H).'    
      x-ngsi:    
        type: Relationship    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    designDischarge:    
      description: 'The design discharge (Qo) of the Spillway'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: ' m^3/s.'    
    designDischargeCoefficient:    
      description: 'The discharge coefficient (Co) for energy losses for the design discharge (Ho).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    designHead:    
      description: 'The total upstream energy head for which the spillway is designed (Ho) for ''Ogee Spillway'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    dischargeCoefficient:    
      description: 'The discharge coefficient for energy losses as water enters, flows and exits the spillway'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: m^0.5/s.    
    id:    
      anyOf: &spillway_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    maxFloodElevation:    
      description: 'The maximum elevation of water that can pass the spillway.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numberAbutments:    
      description: 'The number of abutments of an ogee spillway. Only for ''Ogee'' type.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *spillway_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    spillwayType:    
      description: 'The type of the spillway. In the case of “Specified Spillway”, only “Elevation – discharge” curve is required. Enum:''Broad-Crested, Ogee, Sharp-Crested, Specified Spillway''.'    
      enum:    
        - Broad-Crested    
        - Ogee    
        - Sharp-Crested    
        - 'Specified Spillway'    
      type: string    
      x-ngsi:    
        type: Property    
    spillwayWidth:    
      description: 'The width of the spillway (m). Only for ''Broad-Crested'' type'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters.    
    tag:    
      description: 'An optional text string used to qualify an item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity Type. It has to be Spillway.'    
      enum:    
        - Spillway    
      type: string    
      x-ngsi:    
        type: Property    
    waterDischarge:    
      description: 'The discharge over the spillway (Q)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: ' m^3/s'    
  required:    
    - id    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/Spillway/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/Spillway/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### Spillway NGSI-v2 key-values Example    
Here is an example of a Spillway in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Spillway:id:FFPG:06271993",  
  "type": "Spillway",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      60.3603485,  
      -129.682253  
    ]  
  },  
  "address": {  
    "streetAddress": "",  
    "addressLocality": "",  
    "addressRegion": "",  
    "addressCountry": "",  
    "postalCode": "",  
    "postOfficeBoxNumber": "",  
    "areaServed": ""  
  },  
  "areaServed": "",  
  "dateCreated": "2020-10-12T04:27:47Z",  
  "dateModified": "2021-09-26T16:22:05Z",  
  "source": "",  
  "name": "SP01",  
  "alternateName": "SP01 - Thivae",  
  "description": "Spillway 01 - Thivae",  
  "dataProvider": "EYDAP",  
  "owner": [  
    "urn:ngsi-ld:Spillway:items:OFPV:04640010",  
    "urn:ngsi-ld:Spillway:items:BFAT:33357858"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Spillway:items:VLIF:47226224",  
    "urn:ngsi-ld:Spillway:items:BDSZ:68275691"  
  ],  
  "tag": "",  
  "spillwayType": "Ogee",  
  "crestElevation": 26.4,  
  "crestLength": 5,  
  "spillwayWidth": 5,  
  "numberAbutments": 2,  
  "apronElevation": 22,  
  "apronLength": 5,  
  "dischargeCoefficient": 5,  
  "designHead": 30.4,  
  "designDischarge": 20,  
  "designDischargeCoefficient": 0.4,  
  "maxFloodElevation": 4,  
  "waterDischarge": 9,  
  "controlCrossSection": "urn:ngsi-ld:Spillway:controlCrossSection:JXFD:60487647",  
  "curveElevationDischarge": "urn:ngsi-ld:Spillway:curveElevationDischarge:CBWI:21948924",  
  "curveDischargeCoefficient": "urn:ngsi-ld:Spillway:curveDischargeCoefficient:MWGU:81565938",  
  "curveDesignDischargeCoefficient": "urn:ngsi-ld:Spillway:curveDesignDischargeCoefficient:GIWE:80160975"  
}  
```  
</details>  
#### Spillway NGSI-v2 normalized Example    
Here is an example of a Spillway in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Spillway:id:FFPG:06271993",  
  "type": "Spillway",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        60.3603485,  
        -129.682253  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "streetAddress": "",  
      "addressLocality": "",  
      "addressRegion": "",  
      "addressCountry": "",  
      "postalCode": "",  
      "postOfficeBoxNumber": "",  
      "areaServed": ""  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": ""  
  },  
  "dateCreated":{  
      "type": "DateTime",  
      "value": "2020-10-12T04:27:47Z"  
  },  
  "dateModified": {  
      "type": "DateTime",  
      "value": "2021-09-26T16:22:05Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "SP01"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "SP01 - Thivae"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Spillway 01 - Thivae"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Spillway:items:OFPV:04640010",  
      "urn:ngsi-ld:Spillway:items:BFAT:33357858"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Spillway:items:VLIF:47226224",  
      "urn:ngsi-ld:Spillway:items:BDSZ:68275691"  
    ]  
  },  
  "tag": {  
    "type": "Text",  
    "value": ""  
  },  
  "spillwayType": {  
    "type": "Text",  
    "value": "Ogee"  
  },  
  "crestElevation": {  
    "type": "Number",  
    "value": 26.4  
  },  
  "crestLength": {  
    "type": "Number",  
    "value": 5  
  },  
  "spillwayWidth": {  
    "type": "Number",  
    "value": 5  
  },  
  "numberAbutments": {  
    "type": "Number",  
    "value": 2  
  },  
  "apronElevation": {  
    "type": "Number",  
    "value": 22  
  },  
  "apronLength": {  
    "type": "Number",  
    "value": 5  
  },  
  "dischargeCoefficient": {  
    "type": "Number",  
    "value": 5  
  },  
  "designHead": {  
    "type": "Number",  
    "value": 30.4  
  },  
  "designDischarge": {  
    "type": "Number",  
    "value": 20  
  },  
  "designDischargeCoefficient": {  
    "type": "Number",  
    "value": 0.4  
  },  
  "maxFloodElevation": {  
    "type": "Number",  
    "value": 4  
  },  
  "waterDischarge": {  
    "type": "Number",  
    "value": 9  
  },    
  "controlCrossSection": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Spillway:controlCrossSection:JXFD:60487647"  
  },  
  "curveElevationDischarge": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Spillway:curveElevationDischarge:CBWI:21948924"  
  },  
  "curveDischargeCoefficient": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Spillway:curveDischargeCoefficient:MWGU:81565938"  
  },  
  "curveDesignDischargeCoefficient": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Spillway:curveDesignDischargeCoefficient:GIWE:80160975"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### Spillway NGSI-LD key-values Example    
Here is an example of a Spillway in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Spillway:id:FFPG:06271993",  
    "type": "Spillway",  
    "address": {  
        "streetAddress": "",  
        "addressLocality": "",  
        "addressRegion": "",  
        "addressCountry": "",  
        "postalCode": "",  
        "postOfficeBoxNumber": "",  
        "areaServed": ""  
    },  
    "alternateName": "SP01 - Thivae",  
    "apronElevation": 22,  
    "apronLength": 5,  
    "areaServed": "",  
    "controlCrossSection": "urn:ngsi-ld:Spillway:controlCrossSection:JXFD:60487647",  
    "crestElevation": 26.4,  
    "crestLength": 5,  
    "curveDesignDischargeCoefficient": "urn:ngsi-ld:Spillway:curveDesignDischargeCoefficient:GIWE:80160975",  
    "curveDischargeCoefficient": "urn:ngsi-ld:Spillway:curveDischargeCoefficient:MWGU:81565938",  
    "curveElevationDischarge": "urn:ngsi-ld:Spillway:curveElevationDischarge:CBWI:21948924",  
    "dataProvider": "EYDAP",  
    "dateCreated": "2020-10-12T04:27:47Z",  
    "dateModified": "2021-09-26T16:22:05Z",  
    "description": "Spillway 01 - Thivae",  
    "designDischarge": 20,  
    "designDischargeCoefficient": 0.4,  
    "designHead": 30.4,  
    "dischargeCoefficient": 5,  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            60.3603485,  
            -129.682253  
        ]  
    },  
    "maxFloodElevation": 4,  
    "name": "SP01",  
    "numberAbutments": 2,  
    "owner": [  
        "urn:ngsi-ld:Spillway:items:OFPV:04640010",  
        "urn:ngsi-ld:Spillway:items:BFAT:33357858"  
    ],  
    "seeAlso": [  
        "urn:ngsi-ld:Spillway:items:VLIF:47226224",  
        "urn:ngsi-ld:Spillway:items:BDSZ:68275691"  
    ],  
    "source": "",  
    "spillwayType": "Ogee",  
    "spillwayWidth": 5,  
    "tag": "",  
    "waterDischarge": 9,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Spillway NGSI-LD normalized Example    
Here is an example of a Spillway in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Spillway:id:FFPG:06271993",  
    "type": "Spillway",  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "",  
            "addressLocality": "",  
            "addressRegion": "",  
            "addressCountry": "",  
            "postalCode": "",  
            "postOfficeBoxNumber": "",  
            "areaServed": ""  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "SP01 - Thivae"  
    },  
    "apronElevation": {  
        "type": "Property",  
        "value": 22  
    },  
    "apronLength": {  
        "type": "Property",  
        "value": 5  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "controlCrossSection": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Spillway:controlCrossSection:JXFD:60487647"  
    },  
    "crestElevation": {  
        "type": "Property",  
        "value": 26.4  
    },  
    "crestLength": {  
        "type": "Property",  
        "value": 5  
    },  
    "curveDesignDischargeCoefficient": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Spillway:curveDesignDischargeCoefficient:GIWE:80160975"  
    },  
    "curveDischargeCoefficient": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Spillway:curveDischargeCoefficient:MWGU:81565938"  
    },  
    "curveElevationDischarge": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Spillway:curveElevationDischarge:CBWI:21948924"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "EYDAP"  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-10-12T04:27:47Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-09-26T16:22:05Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Spillway 01 - Thivae"  
    },  
    "designDischarge": {  
        "type": "Property",  
        "value": 20  
    },  
    "designDischargeCoefficient": {  
        "type": "Property",  
        "value": 0.4  
    },  
    "designHead": {  
        "type": "Property",  
        "value": 30.4  
    },  
    "dischargeCoefficient": {  
        "type": "Property",  
        "value": 5  
    },  
    "location": {  
        "type": "Geoproperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                60.3603485,  
                -129.682253  
            ]  
        }  
    },  
    "maxFloodElevation": {  
        "type": "Property",  
        "value": 4  
    },  
    "name": {  
        "type": "Property",  
        "value": "SP01"  
    },  
    "numberAbutments": {  
        "type": "Property",  
        "value": 2  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:Spillway:items:OFPV:04640010",  
            "urn:ngsi-ld:Spillway:items:BFAT:33357858"  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:Spillway:items:VLIF:47226224",  
            "urn:ngsi-ld:Spillway:items:BDSZ:68275691"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "spillwayType": {  
        "type": "Property",  
        "value": "Ogee"  
    },  
    "spillwayWidth": {  
        "type": "Property",  
        "value": 5  
    },  
    "tag": {  
        "type": "Property",  
        "value": ""  
    },  
    "waterDischarge": {  
        "type": "Property",  
        "value": 9  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
