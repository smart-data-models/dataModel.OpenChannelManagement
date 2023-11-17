<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: OpenChannelJunction    
===========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/OpenChannelJunction/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Questa entità contiene una descrizione armonizzata di una giunzione generica realizzata per il dominio di gestione del sistema delle acque grezze (canali aperti). Una giunzione definisce un punto in cui le caratteristiche del canale cambiano, due o più canali si uniscono o si separano, quantità di acqua vengono estratte o inserite nel sistema, ecc.**.    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `downstreamNode[*]`: Una relazione che indica l'ID del nodo a valle (ad es., nodo, struttura di regolazione), dove termina il canale.  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `observedBy[*]`: Una relazione con l'ID del dispositivo che monitora le proprietà dell'acqua grezza.  . Model: [https://smart-data-models.github.io/dataModel.Device/device-schema.json](https://smart-data-models.github.io/dataModel.Device/device-schema.json)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `position[object]`: Oggetto che fornisce informazioni sulla distanza con il resto degli elementi e sulla relazione con essi.  	- `distance[number]`: La distanza tra questa entità e un punto di riferimento (ad esempio, il punto più a monte del sistema).      
- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `tag[string]`: Una stringa di testo facoltativa utilizzata per qualificare un elemento.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo di entità NGSI. deve essere OpenChannelJunction.  - `uniqueName[string]`: Il nome della giunzione  - `upstreamNode[*]`: Una relazione che indica l'ID del nodo a monte (ad es., nodo, struttura di regolazione), dove inizia il canale.  - `waterInflow[number]`: Flusso d'acqua inserito nella giunzione  - `waterLevel[number]`: Livello dell'acqua all'incrocio  - `waterOutflow[number]`: Flusso d'acqua prelevato dal raccordo o deviato verso un'altra fonte  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
OpenChannelJunction:      
  description: 'This entity contains a harmonised description of a generic Junction made for Raw-Water (Open Channels) System Management domain. A Junction defines a location where the characteristics of the channel changes, two or more channels come together or split apart, amounts of water are abstracted or inserted to the system etc.'      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    downstreamNode:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: 'A relationship indicating the ID of the downstream node (e.g., Junction, Regulation Structure), where the channel ends'      
      x-ngsi:      
        type: Relationship      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    observedBy:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: A relationship to the ID of the device that monitors raw-water properties      
      x-ngsi:      
        model: https://smart-data-models.github.io/dataModel.Device/device-schema.json      
        type: Relationship      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    position:      
      description: Object providing information about the distance with the rest of the elements and a relationship with them      
      properties:      
        distance:      
          description: 'The distance between this Entity and a reference point (e.g., the most upstream point of the system)'      
          type: number      
          x-ngsi:      
            type: Property      
            units: ' Km'      
        refPoint:      
          anyOf:      
            - description: Identifier format of any NGSI entity      
              maxLength: 256      
              minLength: 1      
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
              type: string      
              x-ngsi:      
                type: Property      
            - description: Identifier format of any NGSI entity      
              format: uri      
              type: string      
              x-ngsi:      
                type: Property      
          description: The reference point distance is measured from      
          x-ngsi:      
            type: Relationship      
      type: object      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    tag:      
      description: An optional text string used to qualify an item      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI Entity Type. it has to be OpenChannelJunction      
      enum:      
        - OpenChannelJunction      
      type: string      
      x-ngsi:      
        type: Property      
    uniqueName:      
      description: The name of the junction      
      type: string      
      x-ngsi:      
        type: Property      
    upstreamNode:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: 'A relationship indicating the ID of the upstream node (e.g., Junction, Regulation Structure), where the channel begins'      
      x-ngsi:      
        type: Relationship      
    waterInflow:      
      description: Water flow inserted to the junction      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: m3/s      
    waterLevel:      
      description: Water level at the junction      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: m      
    waterOutflow:      
      description: Water flow abstracted from the junction or diverted to another source      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: m3/s      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/OpenChannelJunction/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/OpenChannelJunction/schema.json      
  x-model-tags: FIWARE4WATER      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### OpenChannelJunction NGSI-v2 valori-chiave Esempio    
Ecco un esempio di OpenChannelJunction in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelJunction:id:PTOM:78370074",  
  "type": "OpenChannelJunction",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -65.2981945,  
      -22.649102  
    ]  
  },  
  "address": {  
    "streetAddress": "",  
    "addressLocality": "",  
    "addressRegion": "",  
    "addressCountry": "",  
    "postalCode": "",  
    "postOfficeBoxNumber": ""  
  },  
  "areaServed": "",  
  "dateCreated": "1983-10-11T21:04:39Z",  
  "dateModified": "1982-03-03T08:37:57Z",  
  "source": "",  
  "name": "J1",  
  "alternateName": "Thivae",  
  "dataProvider": "EYDAP",  
  "owner": [  
    "urn:ngsi-ld:OpenChannelJunction:items:QPEH:03184806",  
    "urn:ngsi-ld:OpenChannelJunction:items:PUHR:34031741"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:OpenChannelJunction:items:KTWJ:61564622",  
    "urn:ngsi-ld:OpenChannelJunction:items:JOMY:24566116"  
  ],  
  "position": {  
    "distance": 160.6,  
    "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647"  
  },  
  "downstreamNode": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924",  
  "upstreamNode": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938",  
  "observedBy": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975",  
  "uniqueName": "J1",  
  "tag": "",  
  "waterOutflow": 0.12,  
  "waterInflow": 0.15,  
  "waterLevel": 0.85  
}  
```  
</details>    
#### OpenChannelJunction NGSI-v2 normalizzato Esempio    
Ecco un esempio di OpenChannelJunction in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelJunction:id:PTOM:78370074",  
  "type": "OpenChannelJunction",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -65.2981945,  
        -22.649102  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
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
    "value": "1983-10-11T21:04:39Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1982-03-03T08:37:57Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "J1"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Thivae"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Open Channel Junction"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:OpenChannelJunction:items:QPEH:03184806",  
      "urn:ngsi-ld:OpenChannelJunction:items:PUHR:34031741"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:OpenChannelJunction:items:KTWJ:61564622",  
      "urn:ngsi-ld:OpenChannelJunction:items:JOMY:24566116"  
    ]  
  },  
  "position": {  
    "type": "StructuredValue",  
    "value": {  
      "distance": 160.6,  
      "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647"  
    }  
  },  
  "downstreamNode": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924"  
  },  
  "upstreamNode": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938"  
  },  
  "observedBy": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975"  
  },  
  "uniqueName": {  
    "type": "Text",  
    "value": "J1"  
  },  
  "tag": {  
    "type": "Text",  
    "value": ""  
  },  
  "waterOutflow": {  
    "type": "Number",  
    "value": 0.12  
  },  
  "waterInflow": {  
    "type": "Number",  
    "value": 0.15  
  },  
  "waterLevel": {  
    "type": "Number",  
    "value": 0.56  
  }  
}  
```  
</details>    
#### OpenChannelJunction Valori chiave NGSI-LD Esempio    
Ecco un esempio di OpenChannelJunction in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelJunction:id:PTOM:78370074",  
  "type": "OpenChannelJunction",  
  "address": {  
    "streetAddress": "",  
    "addressLocality": "",  
    "addressRegion": "",  
    "addressCountry": "",  
    "postalCode": "",  
    "postOfficeBoxNumber": ""  
  },  
  "alternateName": "Thivae",  
  "areaServed": "",  
  "dataProvider": "EYDAP",  
  "dateCreated": "1983-10-11T21:04:39Z",  
  "dateModified": "1982-03-03T08:37:57Z",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -65.2981945,  
      -22.649102  
    ]  
  },  
  "name": "J1",  
  "owner": [  
    "urn:ngsi-ld:OpenChannelJunction:items:QPEH:03184806",  
    "urn:ngsi-ld:OpenChannelJunction:items:PUHR:34031741"  
  ],  
  "position": {  
    "distance": 160.6,  
    "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647"  
  },  
  "downstreamNode": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924",  
  "upstreamNode": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938",  
  "observedBy": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975",  
  "uniqueName": "J1",  
  "tag": "",  
  "waterOutflow": 0.12,  
  "waterInflow": 0.15,  
  "waterLevel": 0.85,  
  "seeAlso": [  
    "urn:ngsi-ld:OpenChannelJunction:items:KTWJ:61564622",  
    "urn:ngsi-ld:OpenChannelJunction:items:JOMY:24566116"  
  ],  
  "source": "",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### OpenChannelJunction NGSI-LD normalizzato Esempio    
Ecco un esempio di OpenChannelJunction in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:OpenChannelJunction:id:PTOM:78370074",  
    "type": "OpenChannelJunction",  
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
        "value": "Thivae"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "EYDAP"  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1983-10-11T21:04:39Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1982-03-03T08:37:57Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Open Channel Junction"  
    },  
    "downstreamNode": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -65.2981945,  
                -22.649102  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "J1"  
    },  
    "observedBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:OpenChannelJunction:items:QPEH:03184806",  
            "urn:ngsi-ld:OpenChannelJunction:items:PUHR:34031741"  
        ]  
    },  
    "position": {  
        "type": "Property",  
        "value": {  
            "distance": 160.6,  
            "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647"  
        }  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:OpenChannelJunction:items:KTWJ:61564622",  
            "urn:ngsi-ld:OpenChannelJunction:items:JOMY:24566116"  
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
    "uniqueName": {  
        "type": "Property",  
        "value": "J1"  
    },  
    "upstreamNode": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938"  
    },  
    "waterInflow": {  
        "type": "Property",  
        "value": 0.15  
    },  
    "waterOutflow": {  
        "type": "Property",  
        "value": 0.12  
    },  
    "waterLevel": {  
        "type": "Property",  
        "value": 0.56  
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
