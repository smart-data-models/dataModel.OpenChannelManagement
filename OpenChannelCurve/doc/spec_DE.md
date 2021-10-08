Entität: OpenChannelCurve  
=========================









- `id`  

<details><summary><strong>full yaml details</strong></summary>    

OpenChannelCurve:    
  description: 'This entity contains a harmonised description of a generic curve made for Raw-Water (Open Channels) System Management domain.'    
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    curveType:    
      description: 'Type of curve for spillways and regulation structures. It can be a curve representing: 1) the discharge coefficient (C) as a function of relative weir opening (a/H, a: sluice-gate opening, H: upstream head), 2) the discharge (Q) as a function of the water elevation (H), 3) the design discharge coefficient (Co) as a function of P/Ho, where P is the apron elevation of the OGEE spillway and Ho the design upstrean head, 4) discharge coefficient (C) as a function of H/L, where H is the upstream head and L the legnth of a BROAD-CRESTED spillway, 5) the function C/Co - H/Ho. Enum:''C-a/H, H-Q, Co-P/Ho, C-H/L, C/Co-H/Ho'''    
      enum:    
        - a/H-C    
        - H-Q    
        - Co-P/Ho    
        - C-H/L    
        - C/Co-H/Ho    
      type: string    
      x-ngsi:    
        type: Property    
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
    id:    
      anyOf: &openchannelcurve_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *openchannelcurve_-_properties_-_owner_-_items_-_anyof    
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
    tag:    
      description: 'An optional text string used to qualify an item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity Type. It has to be OpenChannelCurve'    
      enum:    
        - OpenChannelCurve    
      type: string    
      x-ngsi:    
        type: Property    
    xData:    
      description: 'X data points for the curve.'    
      items:    
        type: number    
      type: array    
      x-ngsi:    
        type: Property    
    yData:    
      description: 'Y data points for the curve.'    
      items:    
        type: number    
      type: array    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  version: 0.0.1    
```  
</details>    





  "id": "urn:ngsi-ld:OpenChannelCurve:id:FMCV:30717942",  
  "type": "OpenChannelCurve",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -71.481035,  
      -148.255307  
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
  "dateCreated": "2003-09-09T04:19:40Z",  
  "dateModified": "2019-04-13T13:45:31Z",  
  "source": "",  
  "name": "Curve_1",  
  "alternateName": "",  
  "description": "Open Channel Curve for a/H ~ C",  
  "dataProvider": "NTUA",  
  "owner": [  
    "urn:ngsi-ld:OpenChannelCurve:items:EXUV:99745990",  
    "urn:ngsi-ld:OpenChannelCurve:items:HXOV:60683026"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:OpenChannelCurve:items:IZFN:20714900",  
    "urn:ngsi-ld:OpenChannelCurve:items:RDSS:63995745"  
  ],  
  "tag": "a/H ~ C curve",  
  "curveType": "a/H ~ C",  
  "xData": [  
    0.001,  
    0.1,  
    0.2,  
    0.3,  
    0.4,  
    0.5,  
    0.6,  
    0.7  
  ],  
  "yData": [  
    0.61,  
    0.5930,  
    0.5942,  
    0.5988,  
    0.6070,  
    0.6209,  
    0.6395,  
    0.6628  
  ]  
}  
```  




  "id": "urn:ngsi-ld:OpenChannelCurve:id:FMCV:30717942",  
  "type": "OpenChannelCurve",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -71.481035,  
        -148.255307  
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
    "type": "Text",  
    "value": ""  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2003-09-09T04:19:40Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2019-04-13T13:45:31Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Curve_1"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "Open Channel Curve for a/H-C"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "NTUA"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:OpenChannelCurve:items:EXUV:99745990",  
      "urn:ngsi-ld:OpenChannelCurve:items:HXOV:60683026"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:OpenChannelCurve:items:IZFN:20714900",  
      "urn:ngsi-ld:OpenChannelCurve:items:RDSS:63995745"  
    ]  
  },  
  "tag": {  
    "type": "Text",  
    "value": "a/H-C curve"  
  },  
  "curveType": {  
    "type": "Text",  
    "value": "a/H-C"  
  },  
  "xData": {  
    "type": "array",  
    "value": [  
      0.001,  
      0.1,  
      0.2,  
      0.3,  
      0.4,  
      0.5,  
      0.6,  
      0.7  
    ]  
  },  
  "yData": {  
    "type": "array",  
    "value": [  
      0.61,  
      0.5930,  
      0.5942,  
      0.5988,  
      0.6070,  
      0.6209,  
      0.6395,  
      0.6628  
    ]  
  }  
}  
```  




  "id": "urn:ngsi-ld:OpenChannelCurve:id:FMCV:30717942",  
  "type": "OpenChannelCurve",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -71.481035,  
      -148.255307  
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
  "dateCreated": "2003-09-09T04:19:40Z",  
  "dateModified": "2019-04-13T13:45:31Z",  
  "source": "",  
  "name": "Curve_1",  
  "alternateName": "",  
  "description": "Open Channel Curve for a/H ~ C",  
  "dataProvider": "NTUA",  
  "owner": [  
    "urn:ngsi-ld:OpenChannelCurve:items:EXUV:99745990",  
    "urn:ngsi-ld:OpenChannelCurve:items:HXOV:60683026"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:OpenChannelCurve:items:IZFN:20714900",  
    "urn:ngsi-ld:OpenChannelCurve:items:RDSS:63995745"  
  ],  
  "tag": "a/H ~ C curve",  
  "curveType": "a/H ~ C",  
  "xData": [  
    0.001,  
    0.1,  
    0.2,  
    0.3,  
    0.4,  
    0.5,  
    0.6,  
    0.7  
  ],  
  "yData": [  
    0.61,  
    0.5930,  
    0.5942,  
    0.5988,  
    0.6070,  
    0.6209,  
    0.6395,  
    0.6628  
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  




  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -71.481035,  
        -148.255307  
      ]  
    }  
  },  
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
  "areaServed": {  
    "type": "Property",  
    "value": ""  
  },  
  "id": "urn:ngsi-ld:OpenChannelCurve:id:FMCV:30717942",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2003-09-09T04:19:40Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2019-04-13T13:45:31Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "Curve_1"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": ""  
  },  
  "description": {  
    "type": "Property",  
    "value": "Open Channel Curve for a/H ~ C"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "NTUA"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:OpenChannelCurve:items:EXUV:99745990",  
      "urn:ngsi-ld:OpenChannelCurve:items:HXOV:60683026"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:OpenChannelCurve:items:IZFN:20714900",  
      "urn:ngsi-ld:OpenChannelCurve:items:RDSS:63995745"  
    ]  
  },  
  "type": "OpenChannelCurve",  
  "tag": {  
    "type": "Property",  
    "value": "a/H ~ C curve"  
  },  
  "curveType": {  
    "type": "Property",  
    "value": "a/H ~ C"  
  },  
  "xData": {  
    "type": "Property",  
    "value": [  
      0.001,  
      0.1,  
      0.2,  
      0.3,  
      0.4,  
      0.5,  
      0.6,  
      0.7  
    ]  
  },  
  "yData": {  
    "type": "Property",  
    "value": [  
      0.61,  
      0.5930,  
      0.5942,  
      0.5988,  
      0.6070,  
      0.6209,  
      0.6395,  
      0.6628  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  