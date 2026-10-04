/* (Beta) Export of data model SluiceGate of the subject dataModel.OpenChannelManagement for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE flowType_type AS ENUM ('Free-Flow', 'Overflow', 'Submerged-Flow');
CREATE TYPE SluiceGate_type AS ENUM ('SluiceGate');
CREATE TABLE SluiceGate (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "curveDischargeCoefficient" JSON,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "downstreamControlPoint" JSON,
  "downstreamEndControlPoint" JSON,
  "flowType" flowType_type,
  "gateBottomElevation" NUMERIC,
  "gateDischargeCoefficient" NUMERIC,
  "gateOpening" NUMERIC,
  "gateWidth" NUMERIC,
  "headDifference" NUMERIC,
  "id" TEXT PRIMARY KEY,
  "location" JSON,
  "name" TEXT,
  "observedBy" JSON,
  "orificeDischargeCoefficient" NUMERIC,
  "owner" JSON,
  "seeAlso" JSON,
  "source" TEXT,
  "tag" TEXT,
  "type" SluiceGate_type,
  "upstreamControlPoint" JSON,
  "upstreamEndControlPoint" JSON,
  "waterDischarge" NUMERIC
);