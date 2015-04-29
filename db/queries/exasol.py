queries = {
    "column": {
        "head": "select {column} from {table} limit {n};",
        "all": "select {column} from {table};",
        "unique": "select distinct {column} from {table};",
        "sample": "select {column} from {table} order by random() limit {n};"
    },
    "table": {
        "select": "select {columns} from {table};",
        "head": "select * from {table} limit {n};",
        "all": "select * from {table};",
        "unique": "select distinct {columns} from {table};",
        "sample": "select * from {table} order by random() limit {n};"
    },
    "system": {
        "schema_no_system": """
                select
                    column_table
                    , column_name
                    , column_type
                from
                    SYS.EXA_ALL_COLUMNS
                where
                    column_schema not in ('SYS')
                """,
        "schema_with_system": """
                select
                    column_table
                    , column_name
                    , column_type
                from
                    SYS.EXA_ALL_COLUMNS
                where
                    column_schema not in ('SYS')
                """,
        "schema_specified": """
                select
                    column_table
                    , column_name
                    , column_type
                from
                    SYS.EXA_ALL_COLUMNS
                where column_schema in (%s);
                """,
        "foreign_keys_for_table": "select c,c,c from (select 1 as c) where 1=2;",
        "foreign_keys_for_column": "select c,c,c from (select 1 as c) where 1=2;",
        "ref_keys_for_table": "select c,c,c from (select 1 as c) where 1=2;",
    }
}
