/* (Beta) Export of data model SluiceGate of the subject dataModel.OpenChannelManagement for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE flowType_type AS ENUM ('Free-Flow','Overflow','Submerged-Flow');CREATE TYPE SluiceGate_type AS ENUM ('SluiceGate');
CREATE TABLE SluiceGate (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, flowType flowType_type, gateBottomElevation NUMERIC, gateDischargeCoefficient NUMERIC, gateOpening NUMERIC, gateWidth NUMERIC, headDifference NUMERIC, id TEXT PRIMARY KEY, location JSON, name TEXT, orificeDischargeCoefficient NUMERIC, owner JSON, seeAlso JSON, source TEXT, tag TEXT, type SluiceGate_type, waterDischarge NUMERIC);