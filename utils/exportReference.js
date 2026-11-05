// Run with the selected OpenAF runtime: oaf -f utils/exportReference.js -e config=/tmp/reference.json
var config = io.readFileJSON(processExpr().config);
load(config.source + "/js/odoc.js");
var build = io.readFileString(config.source + "/buildos.js");
var mapping = {}, match;
var re = /^\s*"([^"]+)": OPENAF_BUILD_HOME \+ "([^"]+)"/gm;
while ((match = re.exec(build)) !== null) mapping[match[1]] = config.source + match[2];
if (Object.keys(mapping).length < 30) throw "Incomplete upstream ODoc subject mapping";
var docs = new ODocsGen(mapping).getODoc();
io.writeFileJSON(config.output, { subjects: mapping, docs: docs });
