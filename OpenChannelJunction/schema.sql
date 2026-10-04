/* (Beta) Export of data model OpenChannelJunction of the subject dataModel.OpenChannelManagement for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE OpenChannelJunction_type AS ENUM ('OpenChannelJunction');
CREATE TABLE OpenChannelJunction (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "downstreamNode" JSON,
  "id" TEXT PRIMARY KEY,
  "location" JSON,
  "name" TEXT,
  "observedBy" JSON,
  "owner" JSON,
  "position" JSON,
  "seeAlso" JSON,
  "source" TEXT,
  "tag" TEXT,
  "type" OpenChannelJunction_type,
  "uniqueName" TEXT,
  "upstreamNode" JSON,
  "waterInflow" NUMERIC,
  "waterLevel" NUMERIC,
  "waterOutflow" NUMERIC
);