import mysql.connector
from datetime import datetime

# Ya que no hay una columna que sus datos sean unicos, generamos nuestra propia llave combinando dos 
# atributos, 'concept_id' es casi unica, pero tiene datos vacios, entonces la concateno con 'code'.
def get_current_concepts(cnx):
    concepts = {}
    cursor = cnx.cursor()
    query = ("SELECT id, code, concept_id FROM concepts")
    cursor.execute(query)
    for (id, code, concept_id) in cursor:
        if concept_id != None:
            tmp = str(code) + str(concept_id)
            if tmp not in concepts:
                concepts[tmp] = id
        else:
            if code not in concepts:
                concepts[code] = id
    cursor.close()
    return concepts

def add_concepts(concepts, cnx):
    sql = ("""INSERT INTO concepts(
        pxordx,
        oldpxordx,
        codetype,
        concept_class_id,
        concept_id,
        vocabulary_id,
        domain_id,
        track,
        standard_concept,
        code,
        codewithperiods,
        codescheme,
        long_desc,
        short_desc,
        code_status,
        code_change,
        code_change_year,
        code_planned_type,
        code_billing_status,
        code_cms_claim_status,
        sex_cd,
        anat_or_cond,
        poa_code_status,
        poa_code_change,
        poa_code_change_year,
        valid_start_date,
        valid_end_date,
        invalid_reason,
        create_dt)
              VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""")
    values = (
        concepts['pxordx'],
        concepts['oldpxordx'],
        concepts['codetype'],
        concepts['concept_class_id'],
        concepts['concept_id'],
        concepts['vocabulary_id'],
        concepts['domain_id'],
        concepts['track'],
        concepts['standard_concept'],
        concepts['code'],
        concepts['codewithperiods'],
        concepts['codescheme'],
        concepts['long_desc'],
        concepts['short_desc'],
        concepts['code_status'],
        concepts['code_change'],
        concepts['code_change_year'],
        concepts['code_planned_type'],
        concepts['code_billing_status'],
        concepts['code_cms_claim_status'],
        concepts['sex_cd'],
        concepts['anat_or_cond'],
        concepts['poa_code_status'],
        concepts['poa_code_change'],
        concepts['poa_code_change_year'],
        concepts['valid_start_date'],
        concepts['valid_end_date'],
        concepts['invalid_reason'],
        concepts['create_dt'],
    )
    cursor = cnx.cursor()
    cursor.execute(sql, values)
    cnx.commit()
    return cursor.lastrowid

def get_current_vocabularies(cnx):
    vocabularies = {}
    cursor = cnx.cursor()
    query = ("SELECT id, ref FROM vocabularies")
    cursor.execute(query)
    for (id, ref) in cursor:
        if ref not in vocabularies:
            vocabularies[ref] = id
    cursor.close()
    return vocabularies

def add_vocabulary(vocabulary, cnx):
    sql = ("""INSERT INTO vocabularies(ref, name, url, description, status, version)
              VALUES(%s, %s, %s, %s, %s, %s)""")
    values = (
        vocabulary['ref'].strip(),
        vocabulary['name'].strip(),
        vocabulary['url'].strip(),
        vocabulary['description'].strip(),
        vocabulary['status'].strip(),
        vocabulary['version'].strip(),
    )
    cursor = cnx.cursor()
    cursor.execute(sql, values)
    cnx.commit()
    return cursor.lastrowid

def update_task_status(status, uuid, cnx):
    now = datetime.now()
    sql = ("""UPDATE tasks SET status = %s, last_update_date = %s WHERE uuid = %s""")
    values = (
        status,
        now.strftime("%Y-%m-%d %H:%M:%S"),
        uuid,
    )
    cursor = cnx.cursor()
    cursor.execute(sql, values)
    cnx.commit()