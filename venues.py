from __init__ import close_connection, get_connection


class Venue:
    def __init__(self, venue_id):
        self.venue_id = venue_id

    def concerts(self):
        conn = get_connection()
        query = """
        SELECT * FROM concerts 
        WHERE venue_id = %s;
        """
        try:
            with conn.cursor() as cur:
                cur.execute(query, (self.venue_id,))
                return cur.fetchall()
        finally:
            close_connection(conn)

    def bands(self):
        conn = get_connection()
        query = """
        SELECT DISTINCT bands.* 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        WHERE concerts.venue_id = %s;
        """
        try:
            with conn.cursor() as cur:
                cur.execute(query, (self.venue_id,))
                return cur.fetchall()
        finally:
            close_connection(conn)

    def concert_on(self, date):
        conn = get_connection()
        query = """
        SELECT * 
        FROM concerts 
        WHERE venue_id = %s AND date = %s 
        ORDER BY date ASC 
        LIMIT 1;
        """
        try:
            with conn.cursor() as cur:
                cur.execute(query, (self.venue_id, date))
                return cur.fetchone()
        finally:
            close_connection(conn)

    def most_frequent_band(self):
        conn = get_connection()
        query = """
        SELECT bands.*, COUNT(*) AS performance_count 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        WHERE concerts.venue_id = %s 
        GROUP BY bands.id 
        ORDER BY performance_count DESC 
        LIMIT 1;
        """
        try:
            with conn.cursor() as cur:
                cur.execute(query, (self.venue_id,))
                return cur.fetchone()
        finally:
            close_connection(conn)


venues = Venue(1)
print(venues.concerts())
