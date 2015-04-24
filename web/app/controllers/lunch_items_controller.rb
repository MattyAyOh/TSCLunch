class LunchItemsController < ApplicationController
  before_action :set_lunch_item, only: [:show, :edit, :update, :destroy]

  # GET /lunch_items
  # GET /lunch_items.json
  def index
    @lunch_items = LunchItem.all
  end

  # GET /lunch_items/1
  # GET /lunch_items/1.json
  def show
  end

  # GET /lunch_items/new
  def new
    @lunch_item = LunchItem.new
  end

  # GET /lunch_items/1/edit
  def edit
  end

  # POST /lunch_items
  # POST /lunch_items.json
  def create
    @lunch_item = LunchItem.new(lunch_item_params)

    respond_to do |format|
      if @lunch_item.save
        format.html { redirect_to @lunch_item, notice: 'Lunch item was successfully created.' }
        format.json { render :show, status: :created, location: @lunch_item }
      else
        format.html { render :new }
        format.json { render json: @lunch_item.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /lunch_items/1
  # PATCH/PUT /lunch_items/1.json
  def update
    respond_to do |format|
      if @lunch_item.update(lunch_item_params)
        format.html { redirect_to @lunch_item, notice: 'Lunch item was successfully updated.' }
        format.json { render :show, status: :ok, location: @lunch_item }
      else
        format.html { render :edit }
        format.json { render json: @lunch_item.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /lunch_items/1
  # DELETE /lunch_items/1.json
  def destroy
    @lunch_item.destroy
    respond_to do |format|
      format.html { redirect_to lunch_items_url, notice: 'Lunch item was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_lunch_item
      @lunch_item = LunchItem.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def lunch_item_params
      params.require(:lunch_item).permit(:name, :vegetarian, :lunch_id)
    end
end
