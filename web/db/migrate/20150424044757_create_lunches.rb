class CreateLunches < ActiveRecord::Migration
  def change
    create_table :lunches do |t|
      t.string :supplier, null: false
      t.datetime :sign_up_date_time, null: false
      t.string :creator, null: false

      t.timestamps null: false
    end
  end
end
