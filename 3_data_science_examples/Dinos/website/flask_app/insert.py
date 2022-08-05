insert_query = DinosaurDB.insert()

with open('../../cleaned_dino_data.csv', 'r', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    db.execute(
        insert_query,
        [{"name": row[0], "diet": row[1], "lived_in": row[2], "type": row[3], "period_name": row[4]} 
            for row in csv_reader]
    )