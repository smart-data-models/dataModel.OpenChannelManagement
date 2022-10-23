<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Porta di scarico  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/SluiceGate/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di una saracinesca generica realizzata per il dominio di gestione dei sistemi di acqua grezza (canali aperti)**.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `curveDischargeCoefficient[*]`: L'URI di un'entità OpenChannelCurve che rappresenta il coefficiente di scarico (C) in funzione dell'apertura relativa dello sbarramento (apertura dello sbarramento (a) su profondità a monte (H)), C su a/H.  - `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `downstreamControlPoint[*]`: Una relazione che indica l'ID di un'entità di tipo Sezione trasversale, che rappresenta una sezione trasversale in una distanza in cui le condizioni di flusso sono permanenti, a valle della paratoia.  - `downstreamEndControlPoint[*]`: Una relazione che indica l'ID di un'entità di tipo Sezione trasversale, che rappresenta una sezione trasversale appena a valle della paratoia.  - `flowType[string]`: Definisce le condizioni di flusso nel gate. Assume i valori: 'Overflow' (il livello dell'acqua a monte supera il livello della cresta dello sbarramento), 'Free-Flow' (il livello dell'acqua è inferiore al bordo della paratoia), 'Submerged Flow' (la velocità del flusso che passa attraverso la paratoia è regolata dall'apertura della stessa). Enum:'Tracimazione, flusso libero, flusso sommerso'.  - `gateBottomElevation[number]`: Elevazione della parte inferiore (cresta) del cancello.  - `gateDischargeCoefficient[number]`: Coefficiente di scarico della paratoia che tiene conto delle perdite di energia quando l'acqua passa sotto la paratoia.  - `gateOpening[number]`: L'altezza dell'apertura del cancello.  - `gateWidth[number]`: La larghezza della paratoia  - `headDifference[number]`: La differenza tra la profondità a monte e quella a valle.  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `observedBy[*]`: Una relazione con l'ID del dispositivo che monitora le proprietà dell'acqua grezza.  . Model: [https://smart-data-models.github.io/dataModel.Device/device-schema.json](https://smart-data-models.github.io/dataModel.Device/device-schema.json)- `orificeDischargeCoefficient[number]`: Coefficiente di scarico dell'orifizio che tiene conto delle perdite di energia quando l'acqua passa sotto la paratoia e l'acqua di coda a valle aumenta in modo tale che la paratoia non scorre più liberamente.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `tag[string]`: Una stringa di testo opzionale utilizzata per qualificare un elemento.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo di entità NGSI-LD. Deve essere SluiceGate.  - `upstreamControlPoint[*]`: Una relazione che indica l'ID di un'entità di tipo Sezione trasversale, che rappresenta una sezione trasversale in una distanza in cui le condizioni di flusso sono permanenti, a monte della paratoia.  - `upstreamEndControlPoint[*]`: Una relazione che indica l'ID di un'entità di tipo Sezione trasversale, che rappresenta una sezione trasversale a monte della paratoia.  - `waterDischarge[number]`: La portata che supera lo sbarramento (Q).  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SluiceGate:    
  description: 'This entity contains a harmonised description of a generic Sluice Gate made for Raw-Water (Open Channels) System Management domain.'    
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
      description: 'The URI of an OpenChannelCurve entity that represents the Discharge Coefficient (C) as a function of relative weir opening (weir opening (a) over upstream depth(H)), C over a/H.'    
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
    downstreamControlPoint:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of an entity of type Cross Section, representing a cross section in a distance where the flow conditions are permanent, downstream of the sluice gate.'    
      x-ngsi:    
        type: Relationship    
    downstreamEndControlPoint:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of an entity of type Cross Section, representing a cross section just downstream of the sluice gate.'    
      x-ngsi:    
        type: Relationship    
    flowType:    
      description: 'It defines the flow conditions in the gate. It takes the values: ''Overflow'' (upstream water level exceeds the weir crest level), ''Free-Flow'' (water level is lower than gate edge), ''Submerged Flow'' (the rate of flow passing through the gate is regulated by the opening of the gate). Enum:''Overflow, Free-Flow, Submerged-Flow''.'    
      enum:    
        - Free-Flow    
        - Overflow    
        - Submerged-Flow    
      type: string    
      x-ngsi:    
        type: Property    
    gateBottomElevation:    
      description: 'Elevation of the bottom (crest) of the gate.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    gateDischargeCoefficient:    
      description: 'Discharge coefficient of the gate that accounts for energy losses as water passes under the gate.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    gateOpening:    
      description: 'The height of gate opening.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    gateWidth:    
      description: 'The width of the sluice gate'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: ' meters.'    
    headDifference:    
      description: 'The difference between the upstream depth and the depth just downstream.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &sluicegate_-_properties_-_owner_-_items_-_anyof    
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
    observedBy:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship to the ID of the device that monitors raw-water properties'    
      x-ngsi:    
        model: https://smart-data-models.github.io/dataModel.Device/device-schema.json    
        type: Relationship    
    orificeDischargeCoefficient:    
      description: 'Orifice discharge coefficient that accounts for energy losses as water passes under the gate, and the downstream tailwater increases so that the gate is no longer flowing freely.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *sluicegate_-_properties_-_owner_-_items_-_anyof    
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
      description: 'NGSI-LD Entity Type. It has to be SluiceGate.'    
      enum:    
        - SluiceGate    
      type: string    
      x-ngsi:    
        type: Property    
    upstreamControlPoint:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of an entity of type Cross Section, representing a cross section in a distance where the flow conditions are permanent, upstream of the sluice gate.'    
      x-ngsi:    
        type: Relationship    
    upstreamEndControlPoint:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of an entity of type Cross Section, representing a cross section just upstream of the sluice gate.'    
      x-ngsi:    
        type: Relationship    
    waterDischarge:    
      description: 'The discharge that passes the weir (Q).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/SluiceGate/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/SluiceGate/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### SluiceGate NGSI-v2 valori-chiave Esempio  
Ecco un esempio di SluiceGate in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SluiceGate:id:OZDE:42332657",  
  "type": "SluiceGate",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -7.578066,  
      -25.535857  
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
  "dateCreated": "2021-01-13T19:49:28Z",  
  "dateModified": "2021-05-11T14:06:00Z",  
  "source": "",  
  "name": "SG01",  
  "alternateName": "SG01 - Thivae",  
  "description": "Sluic Gate 01 - Thivae",  
  "dataProvider": "EYDAP",  
  "owner": [  
    "urn:ngsi-ld:SluiceGate:items:LXOX:42416570",  
    "urn:ngsi-ld:SluiceGate:items:FSOL:83758025"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SluiceGate:items:ETJS:41829811",  
    "urn:ngsi-ld:SluiceGate:items:IKTE:29167907"  
  ],  
  "tag": "",  
  "gateWidth": 2.5,  
  "gateOpening": 0.5,  
  "gateBottomElevation": 52.3,  
  "gateDischargeCoefficient": 0.5,  
  "orificeDischargeCoefficient": 0.5,  
  "waterDischarge": 9,  
  "headDifference": 1.5,  
  "flowType": "Submerged-Flow",  
  "upstreamEndControlPoint": "urn:ngsi-ld:SluiceGate:upstreamEndControlPoint:JXFD:60487647",  
  "downstreamEndControlPoint": "urn:ngsi-ld:SluiceGate:downstreamEndControlPoint:CBWI:21948924",  
  "upstreamControlPoint": "urn:ngsi-ld:SluiceGate:upstreamControlPoint:MWGU:81565938",  
  "downstreamControlPoint": "urn:ngsi-ld:SluiceGate:downstreamControlPoint:GIWE:80160975",  
  "observedBy": "urn:ngsi-ld:SluiceGate:observedBy:ZWZM:93328711",  
  "curveDischargeCoefficient": "urn:ngsi-ld:SluiceGate:curveDischargeCoefficient:ZPPL:48418583"  
}  
```  
</details>  
#### SluiceGate NGSI-v2 normalizzato Esempio  
Ecco un esempio di SluiceGate in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SluiceGate:id:OZDE:42332657",  
  "type": "SluiceGate",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -7.578066,  
        -25.535857  
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
  "dateCreated": {  
      "type": "DateTime",  
      "value": "1972-01-13T19:49:28Z"  
  },  
  "dateModified":  {  
      "type": "DateTime",  
      "value": "2000-05-11T14:06:00Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "SG01"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "SG01 - Thivae"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Sluice Gate 01 - Thivae"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:SluiceGate:items:LXOX:42416570",  
      "urn:ngsi-ld:SluiceGate:items:FSOL:83758025"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:SluiceGate:items:ETJS:41829811",  
      "urn:ngsi-ld:SluiceGate:items:IKTE:29167907"  
    ]  
  },  
  "tag": {  
    "type": "Text",  
    "value": ""  
  },  
  "gateType": {  
    "type": "Text",  
    "value": "Sluice Gate"  
  },  
  "gateWidth": {  
    "type": "Number",  
    "value": 2.5  
  },  
  "gateOpening": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "gateBottomElevation": {  
    "type": "Number",  
    "value": 52.3  
  },  
  "gateDischargeCoefficient": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "orificeDischargeCoefficient": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "waterDischarge": {  
    "type": "Number",  
    "value": 9  
  },  
  "headDifference": {  
    "type": "Number",  
    "value": 1.5  
  },  
  "flowType": {  
    "type": "Text",  
    "value": "Submerged-Flow"  
  },  
  "upstreamEndControlPoint": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:SluiceGate:upstreamEndControlPoint:JXFD:60487647"  
  },  
  "downstreamEndControlPoint": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:SluiceGate:downstreamEndControlPoint:CBWI:21948924"  
  },  
  "upstreamControlPoint": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:SluiceGate:upstreamControlPoint:MWGU:81565938"  
  },  
  "downstreamControlPoint": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SluiceGate:downstreamControlPoint:GIWE:80160975"  
  },  
  "observedBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:SluiceGate:observedBy:ZWZM:93328711"  
  },  
  "curveDischargeCoefficient": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:SluiceGate:curveDischargeCoefficient:ZPPL:48418583"  
  }  
}  
```  
</details>  
#### SluiceGate NGSI-LD valori-chiave Esempio  
Ecco un esempio di SluiceGate in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SluiceGate:id:OZDE:42332657",  
    "type": "SluiceGate",  
    "address": {  
        "streetAddress": "",  
        "addressLocality": "",  
        "addressRegion": "",  
        "addressCountry": "",  
        "postalCode": "",  
        "postOfficeBoxNumber": "",  
        "areaServed": ""  
    },  
    "alternateName": "SG01 - Thivae",  
    "areaServed": "",  
    "curveDischargeCoefficient": "urn:ngsi-ld:SluiceGate:curveDischargeCoefficient:ZPPL:48418583",  
    "dataProvider": "EYDAP",  
    "dateCreated": "2021-01-13T19:49:28Z",  
    "dateModified": "2021-05-11T14:06:00Z",  
    "description": "Sluic Gate 01 - Thivae",  
    "downstreamControlPoint": "urn:ngsi-ld:SluiceGate:downstreamControlPoint:GIWE:80160975",  
    "downstreamEndControlPoint": "urn:ngsi-ld:SluiceGate:downstreamEndControlPoint:CBWI:21948924",  
    "flowType": "Submerged-Flow",  
    "gateBottomElevation": 52.3,  
    "gateDischargeCoefficient": 0.5,  
    "gateOpening": 0.5,  
    "gateWidth": 2.5,  
    "headDifference": 1.5,  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -7.578066,  
            -25.535857  
        ]  
    },  
    "name": "SG01",  
    "observedBy": "urn:ngsi-ld:SluiceGate:observedBy:ZWZM:93328711",  
    "orificeDischargeCoefficient": 0.5,  
    "owner": [  
        "urn:ngsi-ld:SluiceGate:items:LXOX:42416570",  
        "urn:ngsi-ld:SluiceGate:items:FSOL:83758025"  
    ],  
    "seeAlso": [  
        "urn:ngsi-ld:SluiceGate:items:ETJS:41829811",  
        "urn:ngsi-ld:SluiceGate:items:IKTE:29167907"  
    ],  
    "source": "",  
    "tag": "",  
    "upstreamControlPoint": "urn:ngsi-ld:SluiceGate:upstreamControlPoint:MWGU:81565938",  
    "upstreamEndControlPoint": "urn:ngsi-ld:SluiceGate:upstreamEndControlPoint:JXFD:60487647",  
    "waterDischarge": 9,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### SluiceGate NGSI-LD normalizzato Esempio  
Ecco un esempio di SluiceGate in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SluiceGate:id:OZDE:42332657",  
    "type": "SluiceGate",  
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
        "value": "SG01 - Thivae"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "curveDischargeCoefficient": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SluiceGate:curveDischargeCoefficient:ZPPL:48418583"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "EYDAP"  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1972-01-13T19:49:28Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2000-05-11T14:06:00Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Sluice Gate 01 - Thivae"  
    },  
    "downstreamControlPoint": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SluiceGate:downstreamControlPoint:GIWE:80160975"  
    },  
    "downstreamEndControlPoint": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SluiceGate:downstreamEndControlPoint:CBWI:21948924"  
    },  
    "flowType": {  
        "type": "Property",  
        "value": "Submerged-Flow"  
    },  
    "gateBottomElevation": {  
        "type": "Property",  
        "value": 52.3  
    },  
    "gateDischargeCoefficient": {  
        "type": "Property",  
        "value": 0.5  
    },  
    "gateOpening": {  
        "type": "Property",  
        "value": 0.5  
    },  
    "gateType": {  
        "type": "Property",  
        "value": "Sluice Gate"  
    },  
    "gateWidth": {  
        "type": "Property",  
        "value": 2.5  
    },  
    "headDifference": {  
        "type": "Property",  
        "value": 1.5  
    },  
    "location": {  
        "type": "Geoproperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -7.578066,  
                -25.535857  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "SG01"  
    },  
    "observedBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SluiceGate:observedBy:ZWZM:93328711"  
    },  
    "orificeDischargeCoefficient": {  
        "type": "Property",  
        "value": 0.5  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:SluiceGate:items:LXOX:42416570",  
            "urn:ngsi-ld:SluiceGate:items:FSOL:83758025"  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:SluiceGate:items:ETJS:41829811",  
            "urn:ngsi-ld:SluiceGate:items:IKTE:29167907"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "tag": {  
        "type": "Property",  
        "value": ""  
    },  
    "upstreamControlPoint": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SluiceGate:upstreamControlPoint:MWGU:81565938"  
    },  
    "upstreamEndControlPoint": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SluiceGate:upstreamEndControlPoint:JXFD:60487647"  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
